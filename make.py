import requests
import tarfile
import subprocess
import os.path
import re
import argparse
from distutils.dir_util import copy_tree
from tqdm import tqdm

def download_buidroot(buildroot_arch: str):
    url = "https://buildroot.org/downloads/" + buildroot_arch

    r = requests.head(url)
    file_size = int(r.headers.get('content-length', 0))
    print(f'Size of file: {file_size}')

    response = requests.get(url, stream=True)

    with open(buildroot_arch, "wb") as file:
        with tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024,
                  desc=buildroot_arch, initial=0, ascii=True, miniters=1) as progress_bar:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
                progress_bar.update(len(chunk))
    downloaded_file_size = os.path.getsize(buildroot_arch)
    if downloaded_file_size != file_size:
        raise Exception("Downloaded file size mismatched {} {}".format(downloaded_file_size, file_size))

def extract_here(buildroot_arch: str):
    tar = tarfile.open(buildroot_arch, "r:gz")
    tar.extractall()
    tar.close()

def make_buildroot_config(buildroot: str):
    # make stm32f429_disco_defconfig
    make_process = subprocess.Popen(['make', 'stm32f429_disco_defconfig'], cwd=buildroot, stderr=subprocess.STDOUT)
    if make_process.wait() != 0:
        raise Exception("make config command is FAILED")

def make_image(buildroot: str):
    # make
    make_process = subprocess.Popen('make', cwd=buildroot, stderr=subprocess.STDOUT)
    if make_process.wait() != 0:
        raise Exception("make command is FAILED")

def found_and_replace(param: str, new_param: str, lines):
    pt = r'{}[\s=]'.format(param)
    is_found = False
    for index in range(0, len(lines)):
        line = lines[index]
        m = re.search(pt, line)
        if m:
            print("replace {} -> {}".format(line.strip(), new_param.strip()))
            lines[index] = new_param
            is_found = True
            break
    return is_found

def introduce_dir(buildroot: str, path: str, folder: str):
    dst = buildroot + "/" + path + "/" + folder
    copy_tree(folder, dst)

# let's start here
parser = argparse.ArgumentParser(description="The buildroot configurator script")
parser.add_argument('--buildroot', dest="buildroot", default="buildroot-2021.08")

args = parser.parse_args()

buildroot = args.buildroot
ext = "tar.gz"
buildroot_name = buildroot + "." + ext

if not os.path.isdir(buildroot):
    download_buidroot(buildroot_name)
    extract_here(buildroot_name)

make_buildroot_config(buildroot)

buildroot_config_file = buildroot + "/.config"

with open('configs/buildroot.conf') as file:
    parameters = file.readlines()

with open(buildroot_config_file) as file:
    lines = file.readlines()

for param in parameters:
    var_pt = r'(?:#\s)?(\w+)'
    m = re.search(var_pt, param)
    if m:
        var = m.group(1)
        if not found_and_replace(var, param, lines):
            print("append {}".format(param.strip()))
            lines.append(param)

with open(buildroot_config_file, "w") as f:
    f.writelines(lines)

introduce_dir(buildroot, "board/stmicroelectronics", "stm32f429-disco")
introduce_dir(buildroot, "boot", "afboot-stm32")

make_image(buildroot)