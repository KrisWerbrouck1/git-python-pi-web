# GPIO Interfacing

This chapter introduces the basic interfacing of a GPIO on the Raspberry Pi. First an LED and pushbutton are connected to the Pi. Next these are approached using the gpio command line utility. Last they are interfaced from a python script.

## Pinout of Raspberry Pi

A handy website showing the pinout of the Raspberry Pi can be found at [https://pinout.xyz/](https://pinout.xyz/). It categorizes all pins nicely according to their function. It even has an Arduino compatible pinout for WiringPi [https://pinout.xyz/pinout/wiringpi](https://pinout.xyz/pinout/wiringpi).

![Wiring Pi Pinout](./img/pinout_wiring_pi.png)

Do note that WiringPi uses different pin numbers than the actual processor pins (BCM). Both numbering schemes are supported by wiringpi but it is recommended to the use the wiringpi pinout numbering when using the library or gpio utility.

## Installing WiringPi

Before starting make sure you have python3 installed by executing the command `python3 --version`. It should return a version similar to `Python 3.5.3`.

Do not install the wiringpi library using pip. This will install an unofficial library.

To install the official wiringpi library visit [http://wiringpi.com/download-and-install/](http://wiringpi.com/download-and-install/) or execute the commands below:

```shell
cd
git clone git://git.drogon.net/wiringPi
cd wiringPi
./build
```

If all went well, executing `gpio -v` should result in the following output:

```shell
gpio version: 2.46
Copyright (c) 2012-2018 Gordon Henderson
This is free software with ABSOLUTELY NO WARRANTY.
For details type: gpio -warranty

Raspberry Pi Details:
  Type: Pi 3+, Revision: 03, Memory: 1024MB, Maker: Sony 
  * Device tree is enabled.
  *--> Raspberry Pi 3 Model B Plus Rev 1.3
  * This Raspberry Pi supports user-level GPIO access.
```