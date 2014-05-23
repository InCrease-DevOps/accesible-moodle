#!/usr/bin/python
# -*- coding: utf-8 -*-
from fabric.api import *



def install_prerreq():
    #TODO: avoid to press the y key during install
    sudo("aptitude update")
    sudo("aptitude install apache2")
    sudo("aptitude install apache2")
    sudo("aptitude install mysql-server-5.5") # Pass: vagrant
    #TODO avoid asking for password during mysql server install
    # With this link
    # http://stackoverflow.com/questions/7739645/install-mysql-on-ubuntu-without-password-prompt
    sudo("aptitude install mysql-client")
    sudo("aptitude install mysqltuner")
    #- Configuring the database
    run("mysqltuner --user root --pass vagrant")

def configure_database():
    pass


def configure_apache():
    pass

def install_moodle():
    sudo("aptitude install moodle")
    #Pass db app: moodlepass
    # it will istall moodle config in /etc, 
    import config_moodle
    config_moodle.config_apache_vhost() #better to keep call to fabric here maybe
    #TODO: how to config it? sending the file? creating it remotely by hand?using jinja?
    sude("service apache2 reload")

    

