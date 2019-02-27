# Interfacing with Hardware

<!-- Introduction on the options
  WiringPi
  RPi.GPIO
  C-functions
 -->

The Raspberry Pi has several GPIO (General Purpose Input Output) pins that can be used to connect all kinds of hardware. Using a little software you change their state to be HIGH (`1`) or LOW (`0`) or you can read the value that external hardware is presenting at the input.

## WiringPi Package

WiringPi is a PIN based GPIO access library written in C for the BCM2835, BCM2836 and BCM2837 SoC devices used in all Raspberry Pi. versions. It’s released under the GNU LGPLv3 license and is usable from C, C++ and RTB (BASIC) as well as many other languages with suitable **wrappers**. It’s designed to be familiar to people who have used the Arduino wiring system and is intended for use by experienced C/C++ programmers.

WiringPi includes a command-line utility `gpio` which can be used to program and setup the GPIO pins. You can use this to read and write the pins and even use it to control them from shell scripts.

Some other features of WiringPi:

* WiringPi provides modules to extend wiringPi to use analog interface devices, make use of IO expanders or to use the Pi's serial port to connect to an ATmega (Arduino for example) to extend IO's.
* WiringPi supports analog reading and writing, and while there is no native analog hardware on a Pi by default, modules are provided to support the Gertboards analog chips.

> **Gertboard**
>
> The Gertboard is an add-on GPIO expansion and experimenter board for the Raspberry Pi computer. It comes with a large variety of components, including buttons, LEDs, A/D and D/A converters, a motor controller, and an Atmel ATmega 328p AVR microcontroller which you can program using the standard Arduino IDE (with some minor modifications)

More information about WiringPi can be found at [http://wiringpi.com/](http://wiringpi.com/).

## RPi.PGIO

RPi.PGIO is a Python package that provides a class to control the GPIO pin on a Raspberry Pi.

Note that the current release does not support SPI, I2C, hardware PWM or serial functionality on the RPi yet. This is planned for the near future - watch this space! One-wire functionality is also planned.

Although hardware PWM is not available yet, software PWM is available to use on all channels.

More information about RPi.GPIO can be found at [https://pypi.org/project/RPi.GPIO/](https://pypi.org/project/RPi.GPIO/).

## WiringPi versus RPi.GPIO

WiringPi is a C library while RPi.GPIO is native a Python module. Bindings have been provided for other languages like Python and Java.

WiringPi has the advantage that it comes with a command line utility called `gpio` which can be run by a non-root user. This utility makes it possible to control GPIO pins from the command line. Read about it here: [http://wiringpi.com/the-gpio-utility/](http://wiringpi.com/the-gpio-utility/).

WiringPi doesn't need to be run as root, but programs built with the RPi.GPIO module do need to be run as root.

WiringPi also has a lot more features available such as SPI, I2C, Gert board support, ...

## C-functions

<!-- TODO: Small section on C-functions versus Python -->

## Real-Time Applications

Note that that the Raspberry Pi equipped with Raspbian is unsuitable for real-time or timing critical applications. Linux is a multitasking O/S and another process may be given priority over the CPU, causing jitter in your program.

If you are after true real-time performance and predictability, you need an RTOS (Real-Time Operating System) or a microcontroller setup.