# I2C Interfacing

Connecting a device to another device using I2C is a common practice. This chapter introduces the basics.

## About I2C

The Inter-Integrated Circuit (I2C) protocol is a protocol intended to allow multiple *slave* devices to communicate with one or more *master* chips. I2C is a **two signal wire bus protocol**.

Why I2C? Because

* Its a common standard
  * Easy to use
  * Wide support
* Its "fast" for low-speed devices (100kbit - 400kbit)
* Bus (multiple devices can be connected)
  * Each device connected to the bus is software-addressable by a unique address
* Only 2 communication lines required (SDA and SCL)
  * The SCL and SDA lines are connected to all devices on the I2C bus
* SCL is the clock line.
  * It is used to synchronize all data transfers over the I2C bus.
  * No strict baud rate requirements like for instance with RS232, the master generates a bus clock.
* SDA is the data line.
* There does need to be a third wire which is the ground

<!-- TODO: Image of i2c bus -->

Both SCL and SDA lines are "open drain" drivers. What this means is that the chip can drive its output low, but it cannot drive it high. For the line to be able to go high you must provide pull-up resistors to Vcc. There should be a resistor from the SCL line to Vcc and another from the SDA line to Vcc. You only need one set of pull-up resistors for the whole I2C bus, not for each device. Vcc depends on the devices used.

The devices on the I2C bus are either masters or slaves. The **master is always the device that drives the SCL clock** line. The **slaves are the devices that respond to the master**. There can be, and usually are, multiple slaves on the I2C bus, however there is normally only one master. It is possible to have multiple masters, but it is unusual. A slave cannot initiate a data transfer over the I2C bus, only a master can do that. Both master and slave can transfer data over the I2C bus, but that transfer is always controlled by the master.

## Connecting a Raspberry Pi 3 to an I2C device

When connecting external devices to the Raspberry Pi, voltage levels should always be checked. The **Raspberry Pi runs at 3.3V and is not 5V tolerant**.

Normally I2C requires you to add a pull-up resistor to each line (SDA and SCL). However in the case of a Raspberry Pi 3 you will not need to add these. This because the Raspberry Pi 3 already has pull-ups of 1k8 on each i2c line.

> **HINT** - **Enabling i2c on the Raspberry Pi**
>
> Make sure to enable the i2c bus on the Raspberry Pi. This can be achieved using the `raspi-config` tool by selecting `Interface Options => I2C => Enable`. You may need to restart the device.

## I2c-tools

Before starting with the development of an actual application, its always best to first check if there is connectivity with the hardware. A handy tool at our disposal is **i2cdetect**, which can scan the i2c bus for devices. It is part of a package called **i2c-tools**. This whole package is very useful for debugging and testing.

Install the tools using the following commands:

```shell
sudo apt update
sudo apt install i2c-tools
```

From now on the `i2cdetect` tool can be used to scan the i2c bus and detect connected slave devices. First check the directory `/dev` for available i2c busses

```shell
cd /dev
ls i2c-*
```

Look for `i2c-x` where x is a number

By using`i2cdetect -r <x>` and replacing `<x>` with the number of the actual device bus, the bus can be scanned. For example:

```shell
i2cdetect -r 1
```

You should get output similar to the one shown below if nothing is externally connected.

```text
WARNING! This program can confuse your I2C bus, cause data loss and worse!
I will probe file /dev/i2c-1 using read byte commands.
I will probe address range 0x03-0x77.
Continue? [Y/n]
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

Do note that Linux uses 7-bit addresses for I2C (the R/W LSB-bit is dropped off). That is why it seems that only half of the range is scanned.