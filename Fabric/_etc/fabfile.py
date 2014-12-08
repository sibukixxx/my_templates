# coding:utf-8
from fabric.api import sudo, abort, hide, env, cd
from fabric.decorators import parallel
from fabric.contrib.files import exists

#env.hosts = ['172.18.8.99']
env.user = 'root'
env.key_filename = '~/.ssh/deploy.key'
env.command_timeout = 1800

def anntokate_web():
    _load_conf("anntokate_web")
def asp_web():
    _load_conf("asp_web")
def _load_conf(type):
    execfile( "./_conf/"+type+".conf" )


def do(cmd=""):
    sudo('hostname')
    sudo(cmd)

def df():
    sudo('hostname')
    sudo('df -h')

def ls_la(target="/"):
    sudo('hostname')
    sudo('ls -la '+target)

def cat(target=""):
    sudo('hostname')
    sudo('cat '+target)
