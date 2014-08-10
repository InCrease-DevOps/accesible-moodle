accesible-moodle
================

A collaborative attemp to make the moodle platform more accesible for people with visual impairment and for the implementors of those platforms

## Overview

In this repo you will find the tools and instructions that you will need to quick and easily create a virtual environment with moodle and some accesibility plugins installed.


It is based on virtual box, using Vagrant and python fabric to automaticly install everything you need. After that, your installation can be customized, exported to a more powerfull environment, or just published from your machine.

## Installation

### Simple Install

There is a package available for download, outside of this repo. URL will be here soon.

### Manual Install on Windows 

So far, only windows 64 bit is supported. If you need a 32bit version, just let me know opening an issue on github.com

In the first stage, untill the full installer is ready, you will need a couple of things installed on your computer:

- [Vagrant ](http://www.vagrantup.com/)

- [VirtualBox 4.1 or superior](https://www.virtualbox.org/wiki/Downloads)

- [Python 2.6 or Superior](https://www.python.org/download/)

- [PyCrypto for windows](http://www.voidspace.org.uk/python/modules.shtml) Carefully choose the proper version (latest python 2 for your platform)

Then you will have to [download this repo](https://github.com/juanantoniofm/accesible-moodle/archive/master.zip), unzip it in a folder.
Open a terminal in that folder, and type:

    vagrant up

It will download and install the virtual machine. Note the details on the screen, as this will serve you later to connect to your machine.
You will have to pay a little bit of attention, and accept "Y" some questions that the machine will ask you. 
It will ask also for the password of the database. REMMEMBER it, or note it somewhere.
And the machine will be configured with moodle and its plugins.

Now, to connect to your machine, you have 2 options:

- Connect via ssh or Putty at the port 2222 in localhost, to customize it further

        ssh -p 2222 vagrant@localhost

    The password by default is `vagrant`

- Connect via the Web interface, and start configuring it

    Open a browser, and type the url:

    (localhost:8080)[http://localhost:8080]

And continue customizing your installation, adding modules and courses. 

Let us know your experience, or [open an issue](https://github.com/juanantoniofm/accesible-moodle/issues) if you find any problems.

## Post-Installation

Either after the simple install or the manual one, you will end up with an url. Open it on your browser.
Once you get into the web interface, you will have to perform the initial configuration of the site.

- Accept the license (only if you want)

- select the box "Unattended operation" (if you don't do it, you will have to click "Next" a few times while the moodle installer does it's things)

- You will reach the "Setup Administration Account". Enter the details that you want (don't use "Admin"), and REMEMBER them. Once you are done with the details, go down and click "Update Profile". The system will try to log you in. The default user and  Password will still be "admin" "admin".

- Then, the "New Settings" menu will appear. Here you will have to configure your install with your details.

## Adding your modules, and extending your installation

Now that you have your installation ready, you can continue your way. Use the [Official moodle Documentation](http://docs.moodle.org/27/en/Main_page).

    #TODO: Add information about the guides developed in the project.


