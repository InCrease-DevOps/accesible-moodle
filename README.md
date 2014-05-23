accesible-moodle
================

A collaborative attemp to make the moodle platform more accesible for people with visual impairment and for the implementors of those platforms

## Overview

In this repo you will find the tools and instructions that you will need to quick and easily create a virtual environment with moodle and some accesibility plugins installed.


It is based on virtual box, using Vagrant and python fabric to automaticly install everything you need. After that, your installation can be customized, exported to a more powerfull environment, or just published from your machine.

## Installation

In the first stage, untill the full installer is needed, you will need a couple of things installed on your computer:

- [Vagrant ](http://www.vagrantup.com/)

- [VirtualBox 4.1 or superior](https://www.virtualbox.org/wiki/Downloads)

- [Python 2.6 or Superior](https://www.python.org/download/)

Then you will have to [download this repo](https://github.com/juanantoniofm/accesible-moodle/archive/master.zip), unzip it in a folder.
Open a terminal in that folder, and type:

    vagrant up

It will download and install the virtual machine. Note the details on the screen, as this will serve you later to connect to your machine.

    vagrant provision

And the machine will be configured with moodle and its plugins.

Now, to connect to your machine, you have 2 options:

- Connect via ssh or Putty at the port 2222 in localhost, to customize it further

        ssh -p 2222 vagrant@localhost

    The password by default is `vagrant`

- Connect via the Web interface, and start configuring it

    Open a browser, and type the url:

    (http://localhost:8080)[http://localhost:8080]

And continue customizing your installation, adding modules and courses. 

Let us know your experience, or [open an issue](https://github.com/juanantoniofm/accesible-moodle/issues) if you find any problems.
