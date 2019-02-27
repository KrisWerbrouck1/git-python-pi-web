# LAMP Server

The Raspberry Pi is just a Linux machine. It is possible to run any software that could be executed on other systems like laptops, desktops or even server. This enables the Raspberry Pi to function as a Web server to host modern web applications or websites. A webserver consists out of many components and technologies that work together to function. A common setup is called the LAMP stack. LAMP consists out of open-source software and is an acronym for:

* **L**inux: The operating system that is used
* **A**pache: a webserver that speaks the HTTP protocol
* **M**ySQL: A database that will manage data
* **P**HP: A programming language that enables to build dynamic webpages on the server

![LAMP stack](./img/lamp-stack.jpg)

Linux is already available on the Raspberry Pi in the form of the Raspbian distribution. Therefor it is not necessary to explicitly install this on the Raspberry Pi.

## Installing LAMP components

Before we can start and make use of the LAMP stack, we need to install all the components separately. The best way to do this is to  use the terminal with a set of commands.

> #### tasksel
>
> Some Linux distributions come with a tool called `tasksel`. Tasksel enables you to select the tasks that you would like to execute on the system. This tool has an option to install the full LAMP stack with only a single command. The Rasperry Pi with Raspbion however does not support this tool at the moment. 

### Updating Raspbian

First we need to update Raspbian operating system to the latest version. This can be done with the following commands:

```shell
sudo apt update
sudo apt upgrade -y
```

Once ready, you can continue with the installation of all the LAMP components.
