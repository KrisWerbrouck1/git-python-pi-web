# The Raspberry Pi

The Raspberry Pi is a series of small single-board computers developed in the United Kingdom by the Raspberry Pi Foundation to promote the teaching of basic computer science in schools and in developing countries. The original model became far more popular than anticipated, selling outside of its target market for uses such as robotics. Peripherals (including keyboards, mice and cases) are not included with the Raspberry Pi. Some accessories however have been included in several official and unofficial bundles.

According to the Raspberry Pi Foundation, over 5 million Raspberry Pi's have been sold before February 2015, making it the best-selling British computer. By November 2016 they had sold 11 million units, reaching 12.5m in March 2017, making it the third best-selling "general purpose computer" ever. In July 2017 it was announced that the total sales have now reached nearly 15 million units.

## Specs

The latest in line are the Raspberry Pi 3 and the Raspberry Pi Zero W

**The Raspberry Pi 3**:

* ARMv8-A (64/32-bit) architecture
* Broadcom BCM2837 SoC
* 1.2 GHz 64-bit quad-core ARM Cortex-A53 processor
* Broadcom VideoCore IV @ 250 MHz (BCM2837: 3D part of GPU @ 300 MHz, video part of GPU @ 400 MHz)
* OpenGL ES 2.0 (BCM2835, BCM2836: 24 GFLOPS / BCM2837: 28.8 GFLOPS)
* MPEG-2 and VC-1 (with license), 1080p30 H.264/MPEG-4 AVC high-profile decoder and encoder (BCM2837: 1080p60)
* 1GB of SDRAM (shared with GPU)
* 4 USB 2.0 ports (via the on-board 5-port USB hub)
* 15-pin MIPI camera interface (CSI) connector, used with the Raspberry Pi camera or Raspberry Pi NoIR camera
* HDMI (rev 1.3), composite video (3.5 mm TRRS jack), MIPI display interface (DSI) for raw LCD panels
* MicroSDHC slot
* 10/100 Mbit/s Ethernet, 802.11n wireless, Bluetooth 4.1
* 17 GPIO's

It draws 300 mA (1.5 W) average when idle, 1.34 A (6.7 W) maximum under stress (monitor, keyboard, mouse and WiFi connected).

![The Raspberry Pi 3](./img/raspberry_pi_3.jpg)

**The Raspberry Pi Zero W**:

* ARMv6Z (32-bit) architecture
* Broadcom BCM2835 SoC
* 1 GHz single-core ARM1176JZF-S processor
* Broadcom VideoCore IV @ 250 MHz (BCM2837: 3D part of GPU @ 300 MHz, video part of GPU @ 400 MHz)
* OpenGL ES 2.0 (BCM2835, BCM2836: 24 GFLOPS / BCM2837: 28.8 GFLOPS)
* MPEG-2 and VC-1 (with license), 1080p30 H.264/MPEG-4 AVC high-profile decoder and encoder (BCM2837: 1080p60)
* 500MB of SDRAM (shared with GPU)
* 1 Micro-USB (direct from BCM2835 chip)
* MIPI camera interface (CSI)
* Mini-HDMI, 1080p60, composite video via marked points on PCB for optional header pins
* Audio via Mini-HDMI, stereo audio through PWM on GPIO
* MicroSDHC slot
* 802.11n wireless, Bluetooth 4.1
* 17 GPIO's

It draws 100 mA (0.5 W) average when idle, 350 mA (1.75 W) maximum under stress (monitor, keyboard and mouse connected).

![The Raspberry Pi Zero W](./img/PI-Zero-W-Wireless-Antenna.jpg)

## RPi Operating Systems

The Raspberry Pi foundation provides several ready to use operating system images for the Pi. At the moment of this writing the following are available:

* **Raspbian** - The Foundation's official supported operating system (Debian Jessie)
* **Ubuntu Mate** - Official Ubuntu flavor featuring the MATE desktop
* **Snappy Ubuntu Core** - A new, transactionally-updated Ubuntu for IoT devices, clouds and more
* **OSMC** - Open Source Media Centre
* **OPENELEC** - Open Embedded Linux Entertainment Centre
* **PINET** - Raspberry Pi Classroom Management Solution
* **Windows 10 IoT Core**
* **RISC OS** - A non-Linux distribution

## Setting up the Raspberry Pi with Raspbian

For this course we will be using the Raspbian image. While Ubuntu Mate features a nicer graphical environment, Raspbian is the most widely-supported OS.

While the instructions further on are based on how to equip the Raspberry Pi with Raspbian, they are very similar for most other distributions.

### Creating a bootable SD card

You can download the latest image of Raspbian via the Raspberry Pi website ([https://www.raspberrypi.org/downloads/](https://www.raspberrypi.org/downloads/)). Make sure to pick the "Raspbian Stretch with Desktop" edition. You can leave the zipped file as is, the SD card flash tool extracts it automatically.

> **INFO** - **Lite and Desktop Edition**
>
> The Lite edition of Raspbian is the one without a graphical desktop environment. If you were to attach a display to the Raspberry Pi, all you would see would be a TTY with a login prompt. If you require a GUI, you need to download the normal Desktop image.

The current Raspbian version at the moment of this writing is of November with a Linux kernel version of 4.14. You can always check out the release notes on [http://downloads.raspberrypi.org/raspbian/release_notes.txt](http://downloads.raspberrypi.org/raspbian/release_notes.txt).

To boot the Linux distribution, the image needs to be written to an SD card of at least 4GB. A popular tool to write an image to an SD card is **Etcher**, which can be downloaded at [https://etcher.io/](https://etcher.io/).

> **INFO** - **Other host operating systems**
>
> Check out [http://www.raspberrypi.org/documentation/installation/installing-images/README.md](http://www.raspberrypi.org/documentation/installation/installing-images/README.md) for instructions on deploying the image to an SD card when using a different host operating system such as Linux or Mac.

Make sure to select the correct device letter as a target and load the Linux image from your local drive as shown in the image below. If you're ready, hit the flash button and grab a cup of coffee.

![Etcher](./img/etcher.png)

Once the write process is finished, you can remove the SD card from the computer, and plug it into the Raspberry Pi.

### A Graphical Desktop Environment

If you deployed an OS such as Raspbian than you can attach an HDMI display or RCA Video compatible device (yellow connector on the older Raspberry Pi boards). You will also have to connect a USB keyboard to the RPi to be able to control it. Depending on the operating system and the edition (normal or lite), you will get a graphical desktop environment or a tty terminal.

![Raspbian Graphical Desktop Environment](./img/raspbian_gui.jpg)
