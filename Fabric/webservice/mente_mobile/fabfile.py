# coding:utf-8
from fabric.api import run, sudo, abort, hide, local, env
from fabric.decorators import runs_once
from fabric.contrib.files import exists
import os.path
import datetime

hta_root_path = "/DocumentRoot/mobile/app/webroot/"
normal_hta_path = hta_root_path+".htaccess"
mente_hta_path = hta_root_path+".htaccess_mente"
backup_hta_path = hta_root_path+".htaccess_mente_bak"

def develop():
	# 設定ファイル読み込み
	_load_conf("develop")
def production():
	# 設定ファイル読み込み
	_load_conf("production")
def staging():
	# 設定ファイル読み込み
	_load_conf("staging")
def _load_conf(type):
	execfile( "../_conf/"+type+".conf" )

def mente(switch=""):
	if switch=="" or ( switch!="on" and switch!="off" ):
		abort("usage fab [option] mente:[on/off]")

	print "execute mente '"+switch+"'"

	if switch=="on":
		if exists(backup_hta_path) :
			abort(backup_hta_path+" exists. Already mente on !!")
		if not exists(mente_hta_path) :
			abort(mente_hta_path+" not exists. Fatal error.")

		run("mv {0} {1}".format(normal_hta_path, backup_hta_path))	
		run("mv {0} {1}".format(mente_hta_path, normal_hta_path))	

		print "switch done. now mente 'ON'"
	elif switch=="off":
		if not exists(backup_hta_path) :
			abort(backup_hta_path+" not exists. Already mente off !!")

		run("mv {0} {1}".format(normal_hta_path, mente_hta_path))	
		run("mv {0} {1}".format(backup_hta_path, normal_hta_path))	

		print "switch done. now mente 'OFF'"


def status():
	if exists(backup_hta_path):
		print "status: mente 'ON'"
	elif exists(mente_hta_path):
		print "status: mente 'OFF'"
	else:
		print "Fatal error. "+mente_hta_path+" not exists."
