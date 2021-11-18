# stm32f429_disco1_uclinux

The simple script to configurate the buildroot for the stm32f429i-disc1 (stm32f4-discovery) board. <br />
It takes the latest Linux kernel (5.15.2 version for now) and patches by parameters that reduce the image size.

## how to build

just execute the command:
```
python make.py
```
it downloads the buildroot, extracts this one and patches with needed configuration for the stm32f429 disco1 board.

## how to flash

when the image is built, just execute the next command:
```
python make --flash
```
after the flash process is done, reset the board

## board pic
![stm32f429disc1](https://user-images.githubusercontent.com/11336126/142391713-211e9615-c162-4867-8e53-91b61a7d8e65.jpg)

## board loading process
```
[    0.000000] Booting Linux on physical CPU 0x0
[    0.000000] Linux version 5.15.2 (danila@linux-y8k1) (arm-buildroot-uclinux-uclibcgnueabi-gcc.br_real (Buildroot -g9b100d2) 11.1.0, GNU ld (GNU Binutils) 2.32) #2 PREEMPT Thu Nov 18 11:04:1
[    0.000000] CPU: ARMv7-M [410fc241] revision 1 (ARMv7M), cr=00000000
[    0.000000] CPU: unknown data cache, unknown instruction cache
[    0.000000] OF: fdt: Machine model: STMicroelectronics STM32F429i-DISCO board
[    0.000000] Zone ranges:
[    0.000000]   Normal   [mem 0x0000000090000000-0x00000000907fffff]
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000090000000-0x00000000907fffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000090000000-0x00000000907fffff]
[    0.000000] Built 1 zonelists, mobility grouping off.  Total pages: 2032
[    0.000000] Kernel command line: root=/dev/ram
[    0.000000] Dentry cache hash table entries: 1024 (order: 0, 4096 bytes, linear)
[    0.000000] Inode-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)
[    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
[    0.000000] Memory: 7616K/8192K available (1319K kernel code, 277K rwdata, 244K rodata, 65K init, 106K bss, 576K reserved, 0K cma-reserved)
[    0.000000] rcu: Preemptible hierarchical RCU implementation.
[    0.000000] rcu:     RCU event tracing is enabled.
[    0.000000]  Trampoline variant of Tasks RCU enabled.
[    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 10 jiffies.
[    0.000000] NR_IRQS: 16, nr_irqs: 16, preallocated irqs: 16
[    0.000000] /soc/interrupt-controller@40013c00: bank0
[    0.000000] random: get_random_bytes called from 0x081933dd with crng_init=0
[    0.000000] clocksource: arm_system_timer: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 355517175 ns
[    0.000000] ARM System timer initialized as clocksource
[    0.000010] sched_clock: 32 bits at 84MHz, resolution 11ns, wraps every 25565281274ns
[    0.000232] timer@40000c00: STM32 sched_clock registered
[    0.000415] Switching to timer-based delay loop, resolution 11ns
[    0.000570] timer@40000c00: STM32 delay timer registered
[    0.000762] clocksource: timer@40000c00: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 22753100554 ns
[    0.001029] /soc/timer@40000c00: STM32 clockevent driver initialized (32 bits)
[    0.003200] Calibrating delay loop (skipped), value calculated using timer frequency.. 168.00 BogoMIPS (lpj=840000)
[    0.003478] pid_max: default: 4096 minimum: 301
[    0.004193] Mount-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)
[    0.004460] Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)
[    0.017933] rcu: Hierarchical SRCU implementation.
[    0.020510] devtmpfs: initialized
[    0.248491] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
[    0.248748] pinctrl core: initialized pinctrl subsystem
[    0.446578] stm32f429-pinctrl soc:pin-controller@40020000: No package detected, use default one
[    0.471531] stm32f429-pinctrl soc:pin-controller@40020000: GPIOA bank added
[    0.477944] stm32f429-pinctrl soc:pin-controller@40020000: GPIOB bank added
[    0.484200] stm32f429-pinctrl soc:pin-controller@40020000: GPIOC bank added
[    0.490626] stm32f429-pinctrl soc:pin-controller@40020000: GPIOD bank added
[    0.496987] stm32f429-pinctrl soc:pin-controller@40020000: GPIOE bank added
[    0.500610] stm32f429-pinctrl soc:pin-controller@40020000: GPIOF bank added
[    0.509564] stm32f429-pinctrl soc:pin-controller@40020000: GPIOG bank added
[    0.516012] stm32f429-pinctrl soc:pin-controller@40020000: GPIOH bank added
[    0.519806] stm32f429-pinctrl soc:pin-controller@40020000: GPIOI bank added
[    0.526087] stm32f429-pinctrl soc:pin-controller@40020000: GPIOJ bank added
[    0.535030] stm32f429-pinctrl soc:pin-controller@40020000: GPIOK bank added
[    0.535321] stm32f429-pinctrl soc:pin-controller@40020000: Pinctrl STM32 initialized
[    0.744900] stm32-dma 40026000.dma-controller: STM32 DMA driver registered
[    0.774143] stm32-dma 40026400.dma-controller: STM32 DMA driver registered
[    0.797851] clocksource: Switched to clocksource timer@40000c00
[    0.863141] workingset: timestamp_bits=30 max_order=11 bucket_order=0
[    0.867115] io scheduler mq-deadline registered
[    0.867260] io scheduler kyber registered
[    0.885164] STM32 USART driver initialized
[    0.899415] 40011000.serial: ttySTM0 at MMIO 0x40011000 (irq = 34, base_baud = 5250000) is a stm32-usart
[    1.719831] printk: console [ttySTM0] enabled
[    1.816880] stm32_rtc 40002800.rtc: registered as rtc0
[    1.822239] stm32_rtc 40002800.rtc: setting system clock to 2000-01-05T11:04:54 UTC (947070294)
[    1.832153] stm32_rtc 40002800.rtc: Date/Time must be initialized
[    1.867573] i2c_dev: i2c /dev entries driver
[    1.955673] stmpe-i2c 0-0041: stmpe811 detected, chip id: 0x811
[    2.156840] stm32f4-i2c 40005c00.i2c: STM32F4 I2C driver registered
[    2.167929] random: fast init done
[    2.262612] input: gpio-keys as /devices/platform/gpio-keys/input/input0
[    4.809454] Freeing unused kernel image (initmem) memory: 16K
[    4.815178] This architecture does not have kernel memory protection.
[    4.821931] Run /init as init process
Saving random seed: [    5.692764] random: dd: uninitialized urandom read (512 bytes read)
OK

Welcome to STM32
stm32 login: [  273.178704] random: crng init done
root
Password:
Login incorrect
Jan  5 11:37:53 login[40]: invalid password for 'root' on 'console'
stm32 login: root
Password:
Jan  5 11:38:02 login[40]: root login on 'console'
~ # ls /
bin      init     linuxrc  opt      run      tmp
dev      lib      media    proc     sbin     usr
etc      lib32    mnt      root     sys      var
~ #
```
