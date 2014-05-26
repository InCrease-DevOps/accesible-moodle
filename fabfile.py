#!/usr/bin/python
# -*- coding: utf-8 -*-
from fabric.api import *
import fabric.contrib as contrib
import fabtools as fab
import lib.config as configuration

global config 
config = {}

def log_start():
    local("echo $(date +%F:%H:%M) >> ~/been_here")


def check_system():
    run('whoami')
    run("echo $(date +%F:%H:%M) >> ~/been_here")

def confirm(msg = "Continue?"):
    res = prompt(msg + " [Y/n] ")
    if res == "" or res == "Y" or res == "y":
        return True
    else:
        return False

def request_config():
    global config 
    if len(config) == 0:
        for key,question in configuration.custom.iteritems():
            # Ask for new values
            config[key] = prompt(question)
            if config[key] == "":
                #If user press enter, use default
                config[key] = configuration.defaults[key]
    else:
        if confirm("Do you want to rewrite the config?"):
            config = {}
            request_config()
    print ""
    print "Review the new configuration:"
    print "============================="
    for key, question in configuration.custom.iteritems():
        print question + config[key]
    if not confirm():
        request_config()

def get_from_config( parameter = None):
    """returns elements from the config or request them"""
    assert(parameter != None)
    try:
        return config[parameter]
    except KeyError:
        print parameter + " is not configured. launching configurer"
        request_config()
        return get_from_config(parameter)

def install_prerreq():
    # Enable truly non interactive apt-get installs
    sudo("export DEBIAN_FRONTEND=noninteractive")
    sudo("aptitude -q -y update")
    sudo("aptitude -q -y install apache2")
    fab.require.mysql.server(5.5, get_from_config("db_pass"))
    # this will also be used for moodle tocreate the db
    sudo("aptitude -q -y install mysql-client")

def optimize_db():
    sudo("aptitude -q -y install mysqltuner")
    #- Configuring the database
    print "You should run this after having the system up for a few days"
    run("mysqltuner --user root --pass {0}".format(
        prompt("what did you say it was the pass for mysql?: ")))


def pre_configure_moodle():
    """preseed the debconf before installing"""
    #TODO: This method needs to customize the actual parameters
    fab.require.file(path="/home/vagrant/selections-moodle",source="lib/selections-moodle")
    with cd("/home/vagrant/"):
        contrib.files.sed("selections-moodle","secreto",get_from_config("db_pass")) #TODO Me da penica y problemas hacer en moodle.
        #run("sed 's/secreto/{0}/' selections-moodle".format(get_from_config("db_pass")))
        contrib.files.sed("selections-moodle", "moodleurl",get_from_config("url"))
        #run("sed 's/moodleurl/{0}/' selections-moodle".format(get_from_config("url")))
    sudo("cat /home/vagrant/selections-moodle | while read l; do echo $l; echo $l | debconf-set-selections ; done")

def install_moodle():
    sudo("aptitude -q -y install moodle")
    sudo("service apache2 reload")

def post_configure_moodle():
    sudo("cp /etc/moodle/apache.vhost.conf /etc/apache2/sites-available/moodle")
    sudo("a2ensite moodle")
    sudo("apache2ctl configtest")
    sudo("chown www-data:www-data /usr/share/moodle/")
    sudo("service apache2 reload")

