# I2C Interfacing

Connecting a device to another device using I2C is a common practice. This chapter introduces the basics.

## About I2C

The Inter-Integrated Circuit (I2C) protocol is a protocol intended to allow multiple *slave* devices to communicate with one or more *master* chips. I2C is a two signal wire bus protocol.

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