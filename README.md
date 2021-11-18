# stm32f429_disco1_uclinux


## board loading process

[    0.000000] Booting Linux on physical CPU 0x0<br />
[    0.000000] Linux version 5.15.2 (danila@linux-y8k1) (arm-buildroot-uclinux-uclibcgnueabi-gcc.br_real (Buildroot -g9b100d2) 11.1.0, GNU ld (GNU Binutils) 2.32) #2 PREEMPT Thu Nov 18 11:04:1<br />
[    0.000000] CPU: ARMv7-M [410fc241] revision 1 (ARMv7M), cr=00000000<br />
[    0.000000] CPU: unknown data cache, unknown instruction cache<br />
[    0.000000] OF: fdt: Machine model: STMicroelectronics STM32F429i-DISCO board<br />
[    0.000000] Zone ranges:<br />
[    0.000000]   Normal   [mem 0x0000000090000000-0x00000000907fffff]<br />
[    0.000000] Movable zone start for each node<br />
[    0.000000] Early memory node ranges<br />
[    0.000000]   node   0: [mem 0x0000000090000000-0x00000000907fffff]<br />
[    0.000000] Initmem setup node 0 [mem 0x0000000090000000-0x00000000907fffff]<br />
[    0.000000] Built 1 zonelists, mobility grouping off.  Total pages: 2032<br />
[    0.000000] Kernel command line: root=/dev/ram<br />
[    0.000000] Dentry cache hash table entries: 1024 (order: 0, 4096 bytes, linear)<br />
[    0.000000] Inode-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)<br />
[    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off<br />
[    0.000000] Memory: 7616K/8192K available (1319K kernel code, 277K rwdata, 244K rodata, 65K init, 106K bss, 576K reserved, 0K cma-reserved)<br />
[    0.000000] rcu: Preemptible hierarchical RCU implementation.<br />
[    0.000000] rcu:     RCU event tracing is enabled.<br />
[    0.000000]  Trampoline variant of Tasks RCU enabled.<br />
[    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 10 jiffies.<br />
[    0.000000] NR_IRQS: 16, nr_irqs: 16, preallocated irqs: 16<br />
[    0.000000] /soc/interrupt-controller@40013c00: bank0<br />
[    0.000000] random: get_random_bytes called from 0x081933dd with crng_init=0<br />
[    0.000000] clocksource: arm_system_timer: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 355517175 ns<br />
[    0.000000] ARM System timer initialized as clocksource<br />
[    0.000010] sched_clock: 32 bits at 84MHz, resolution 11ns, wraps every 25565281274ns<br />
[    0.000232] timer@40000c00: STM32 sched_clock registered<br />
[    0.000415] Switching to timer-based delay loop, resolution 11ns<br />
[    0.000570] timer@40000c00: STM32 delay timer registered<br />
[    0.000762] clocksource: timer@40000c00: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 22753100554 ns<br />
[    0.001029] /soc/timer@40000c00: STM32 clockevent driver initialized (32 bits)<br />
[    0.003200] Calibrating delay loop (skipped), value calculated using timer frequency.. 168.00 BogoMIPS (lpj=840000)<br />
[    0.003478] pid_max: default: 4096 minimum: 301<br />
[    0.004193] Mount-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)<br />
[    0.004460] Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)<br />
[    0.017933] rcu: Hierarchical SRCU implementation.<br />
[    0.020510] devtmpfs: initialized<br />
[    0.248491] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns<br />
[    0.248748] pinctrl core: initialized pinctrl subsystem<br />
[    0.446578] stm32f429-pinctrl soc:pin-controller@40020000: No package detected, use default one<br />
[    0.471531] stm32f429-pinctrl soc:pin-controller@40020000: GPIOA bank added<br />
[    0.477944] stm32f429-pinctrl soc:pin-controller@40020000: GPIOB bank added<br />
[    0.484200] stm32f429-pinctrl soc:pin-controller@40020000: GPIOC bank added<br />
[    0.490626] stm32f429-pinctrl soc:pin-controller@40020000: GPIOD bank added<br />
[    0.496987] stm32f429-pinctrl soc:pin-controller@40020000: GPIOE bank added<br />
[    0.500610] stm32f429-pinctrl soc:pin-controller@40020000: GPIOF bank added<br />
[    0.509564] stm32f429-pinctrl soc:pin-controller@40020000: GPIOG bank added<br />
[    0.516012] stm32f429-pinctrl soc:pin-controller@40020000: GPIOH bank added<br />
[    0.519806] stm32f429-pinctrl soc:pin-controller@40020000: GPIOI bank added<br />
[    0.526087] stm32f429-pinctrl soc:pin-controller@40020000: GPIOJ bank added<br />
[    0.535030] stm32f429-pinctrl soc:pin-controller@40020000: GPIOK bank added<br />
[    0.535321] stm32f429-pinctrl soc:pin-controller@40020000: Pinctrl STM32 initialized<br />
[    0.744900] stm32-dma 40026000.dma-controller: STM32 DMA driver registered<br />
[    0.774143] stm32-dma 40026400.dma-controller: STM32 DMA driver registered<br />
[    0.797851] clocksource: Switched to clocksource timer@40000c00<br />
[    0.863141] workingset: timestamp_bits=30 max_order=11 bucket_order=0<br />
[    0.867115] io scheduler mq-deadline registered<br />
[    0.867260] io scheduler kyber registered<br />
[    0.885164] STM32 USART driver initialized<br />
[    0.899415] 40011000.serial: ttySTM0 at MMIO 0x40011000 (irq = 34, base_baud = 5250000) is a stm32-usart<br />
[    1.719831] printk: console [ttySTM0] enabled<br />
[    1.816880] stm32_rtc 40002800.rtc: registered as rtc0<br />
[    1.822239] stm32_rtc 40002800.rtc: setting system clock to 2000-01-05T11:04:54 UTC (947070294)<br />
[    1.832153] stm32_rtc 40002800.rtc: Date/Time must be initialized<br />
[    1.867573] i2c_dev: i2c /dev entries driver<br />
[    1.955673] stmpe-i2c 0-0041: stmpe811 detected, chip id: 0x811<br />
[    2.156840] stm32f4-i2c 40005c00.i2c: STM32F4 I2C driver registered<br />
[    2.167929] random: fast init done<br />
[    2.262612] input: gpio-keys as /devices/platform/gpio-keys/input/input0<br />
[    4.809454] Freeing unused kernel image (initmem) memory: 16K<br />
[    4.815178] This architecture does not have kernel memory protection.<br />
[    4.821931] Run /init as init process<br />
Saving random seed: [    5.692764] random: dd: uninitialized urandom read (512 bytes read)<br />
OK<br />

Welcome to STM32<br />
stm32 login: [  273.178704] random: crng init done<br />
root<br />
Password:<br />
Login incorrect<br />
Jan  5 11:37:53 login[40]: invalid password for 'root' on 'console'<br />
stm32 login: root<br />
Password:<br />
Jan  5 11:38:02 login[40]: root login on 'console'<br />
~ # ls /<br />
bin      init     linuxrc  opt      run      tmp<br />
dev      lib      media    proc     sbin     usr<br />
etc      lib32    mnt      root     sys      var<br />
~ #<br />