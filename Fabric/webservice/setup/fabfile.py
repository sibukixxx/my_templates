# coding:utf-8
from fabric.api import run, sudo, env

base_dir = "/mnt/service_code"

env.hosts = ['192.168.1.3']
env.user = 'vagrant'
env.password = "vagrant"

def setup_dir():
	make_dir()
	copy_dir()
	

def make_dir():
	run("mkdir "+base_dir+"/app_data")
	run("mkdir "+base_dir+"/app_data/admin")
	run("mkdir "+base_dir+"/app_data/mobile")
	run("mkdir "+base_dir+"/app_data/ServiceName")

def rm_dir():
	run("rm -rf "+base_dir+"/app_data")

def copy_dir():
	run("cp -Rp "+base_dir+"/DocumentRoot/admin/app/tmp "+base_dir+"/app_data/admin")
	run("cp -Rp "+base_dir+"/DocumentRoot/admin/ftp "+base_dir+"/app_data/admin")
	run("cp -Rp "+base_dir+"/DocumentRoot/mobile/app/tmp "+base_dir+"/app_data/mobile")
	run("cp -Rp "+base_dir+"/DocumentRoot/ServiceName/app/tmp "+base_dir+"/app_data/ServiceName")

def switch_app_data():
	run("mv "+base_dir+"/DocumentRoot/admin/app/tmp  "+base_dir+"/DocumentRoot/admin/app/tmp_")
	run("ln -s "+base_dir+"/app_data/admin/tmp  "+base_dir+"/DocumentRoot/admin/app/tmp")

	run("mv "+base_dir+"/DocumentRoot/admin/ftp  "+base_dir+"/DocumentRoot/admin/ftp_")
	run("ln -s "+base_dir+"/app_data/admin/ftp  "+base_dir+"/DocumentRoot/admin/ftp")

	run("mv "+base_dir+"/DocumentRoot/mobile/app/tmp  "+base_dir+"/DocumentRoot/mobile/app/tmp_")
	run("ln -s "+base_dir+"/app_data/mobile/tmp  "+base_dir+"/DocumentRoot/mobile/app/tmp")

	run("mv "+base_dir+"/DocumentRoot/ServiceName/app/tmp  "+base_dir+"/DocumentRoot/ServiceName/app/tmp_")
	run("ln -s "+base_dir+"/app_data/ServiceName/tmp  "+base_dir+"/DocumentRoot/ServiceName/app/tmp")

def rollback_switch():
	sudo("rm -f "+base_dir+"/DocumentRoot/admin/app/tmp")
	sudo("mv "+base_dir+"/DocumentRoot/admin/app/tmp_ "+base_dir+"/DocumentRoot/admin/app/tmp")

	sudo("rm -f "+base_dir+"/DocumentRoot/admin/ftp")
	sudo("mv "+base_dir+"/DocumentRoot/admin/ftp_ "+base_dir+"/DocumentRoot/admin/ftp")

	sudo("rm -f "+base_dir+"/DocumentRoot/mobile/app/tmp")
	sudo("mv "+base_dir+"/DocumentRoot/mobile/app/tmp_ "+base_dir+"/DocumentRoot/mobile/app/tmp")

	sudo("rm -f "+base_dir+"/DocumentRoot/ServiceName/app/tmp")
	sudo("mv "+base_dir+"/DocumentRoot/ServiceName/app/tmp_ "+base_dir+"/DocumentRoot/ServiceName/app/tmp")

def move_to_releases():
	run("mkdir "+base_dir+"/releases")
	run("mv "+base_dir+"/DocumentRoot "+base_dir+"/releases")
	run("ln -s "+base_dir+"/releases/DocumentRoot "+base_dir+"/DocumentRoot")

