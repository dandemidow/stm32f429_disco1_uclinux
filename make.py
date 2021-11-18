import requests
import tarfile
import subprocess
import os.path
import re
from distutils.dir_util import copy_tree

buildroot = "buildroot-2021.08"
ext = "tar.gz"
buildroot_name = buildroot + "." + ext
url = "https://buildroot.org/downloads/" + buildroot_name

if not os.path.isdir(buildroot):
    response = requests.get(url, stream = True)
    
    text_file = open(buildroot_name, "wb")
    for chunk in response.iter_content(chunk_size=1024):
        text_file.write(chunk)
    text_file.close()
    
    tar = tarfile.open(buildroot_name, "r:gz")
    tar.extractall()
    tar.close()
# make stm32f429_disco_defconfig
make_process = subprocess.Popen(['make', 'stm32f429_disco_defconfig'], cwd=buildroot, stderr=subprocess.STDOUT)
if make_process.wait() != 0:
    print("something_went_wrong")

print("change parameters")

with open('configs/buildroot.conf') as file:
    parameters = file.readlines()

filename = buildroot + "/.config"
with open(filename) as file:
    lines = file.readlines()
    for param in parameters:
        var_pt = r'(?:#\s)?(\w+)'
        m = re.search(var_pt, param)
        if m:
            var = m.group(1)
            print("variable --- {}".format(var))
            pt = r'{}[\s=]'.format(var)
            is_found = False
            for index in range(0, len(lines)):
                line = lines[index]
                m = re.search(pt, line)
                if m:
                    print("find pattern {} -> {}".format(line, param))
                    lines[index] = param
                    is_found = True
                    break
            if not is_found:
                print("parameter not found, append {}".format(param))
                lines.append(param)
                    

with open(filename, "w") as f:
    f.writelines(lines)

fromDirectory = "stm32f429-disco"
toDirectory = buildroot + "/board/stmicroelectronics/stm32f429-disco"

copy_tree(fromDirectory, toDirectory)

fromDirectory = "afboot-stm32"
toDirectory = buildroot + "/boot/afboot-stm32"

copy_tree(fromDirectory, toDirectory)
