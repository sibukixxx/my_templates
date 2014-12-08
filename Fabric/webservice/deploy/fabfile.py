# coding:utf-8
from fabric.api import run, sudo, abort, hide, local, env
from fabric.decorators import runs_once
from fabric.contrib.files import exists
import os.path
import datetime

clone_cmd = "svn --username deploy --password xxxxx checkout https://svn.com/repos/Service/tags/{tag} {dir}"
clear_cache_cmds = [
	'rm -rf /DocumentRoot/app/tmp/cache/models/*',
	'rm -rf /DocumentRoot/app/tmp/cache/persistent/*',
]

check_cache_files = [
	"/DocumentRoot/ServiceName/app/tmp/cache/persistent/myapp_cake_core_file_map",
]

writable_dirs = {
	"ServiceName/app/tmp":"ServiceName/tmp",
}
configs = [
	"ServiceName/app/Config",
        "phpmyadmin/config.inc.php",
]
	
now_datetime = ""


def develop():
	# デプロイ対象
	env.deploy_target = "develop"

	# コンフィグファイル名（レシトク移行期間の一時的なものなので、落ち着いたら削除する）
	env.config_ext = "develop"

	# 設定ファイル読み込み
	_load_conf(env.deploy_target)
	
	# ディレクトリパス
	env.base_dir = "/mnt/Service_production"
	_set_dir_paths()
    
def production():
	# デプロイ対象
	env.deploy_target = "production"

	# コンフィグファイル名（レシトク移行期間の一時的なものなので、落ち着いたら削除する）
	env.config_ext = "production"

	# 設定ファイル読み込み
	_load_conf(env.deploy_target)
	
	# ディレクトリパス
	env.base_dir = "/mnt/Service/code"
	_set_dir_paths()

def production_all():
	# デプロイ対象
	env.deploy_target = "production_all"

	# コンフィグファイル名（レシトク移行期間の一時的なものなので、落ち着いたら削除する）
	#env.config_ext = "production"

	# 設定ファイル読み込み
	_load_conf(env.deploy_target)
	
	# ディレクトリパス
	env.base_dir = "/mnt/Service/code"
	_set_dir_paths()

	# ServiceNameがないので、パスを削除
	global clear_cache_cmds
	clear_cache_cmds = [path for path in clear_cache_cmds if ('ServiceName' in path) == False]
	global check_cache_files
	check_cache_files = [path for path in check_cache_files if ('ServiceName' in path) == False]
	global configs
	configs = [path for path in configs if ('ServiceName' in path) == False]
	global writable_dirs 
	temp = {}
	for key in writable_dirs.keys():
		if ('ServiceName' in key) == False:
			temp[key] = writable_dirs[key]	
	writable_dirs = temp

def prod_anntokate():
	# デプロイ対象
	env.deploy_target = "prod_anntokate"

	# コンフィグファイル名（レシトク移行期間の一時的なものなので、落ち着いたら削除する）
	env.config_ext = "production"

	# 設定ファイル読み込み
	_load_conf(env.deploy_target)
	
	# ディレクトリパス
	env.base_dir = "/mnt/Service_production"
	_set_dir_paths()

	# trackingがないので、パスを削除
	global clear_cache_cmds
	clear_cache_cmds = [path for path in clear_cache_cmds if ('tracking' in path) == False]
	global check_cache_files
	check_cache_files = [path for path in check_cache_files if ('tracking' in path) == False]
	global configs
	configs = [path for path in configs if ('tracking' in path) == False]
	global writable_dirs 
	temp = {}
	for key in writable_dirs.keys():
		if ('tracking' in key) == False:
			temp[key] = writable_dirs[key]	
	writable_dirs = temp

	# ServiceNameがないので、パスを削除
	clear_cache_cmds = [path for path in clear_cache_cmds if ('ServiceName' in path) == False]
	check_cache_files = [path for path in check_cache_files if ('ServiceName' in path) == False]
	configs = [path for path in configs if ('ServiceName' in path) == False]
	temp = {}
	for key in writable_dirs.keys():
		if ('ServiceName' in key) == False:
			temp[key] = writable_dirs[key]	
	writable_dirs = temp

def prod_sssss():
	# デプロイ対象
	env.deploy_target = "prod_sssss"

	env.config_ext = "production"

	# 設定ファイル読み込み
	_load_conf(env.deploy_target)
	
	# ディレクトリパス
	env.base_dir = "/mnt/Service_production"
	_set_dir_paths()

	# trackingがないので、パスを削除
	global clear_cache_cmds
	clear_cache_cmds = [path for path in clear_cache_cmds if ('tracking' in path) == False]
	global check_cache_files
	check_cache_files = [path for path in check_cache_files if ('tracking' in path) == False]
	global configs
	configs = [path for path in configs if ('tracking' in path) == False]
	global writable_dirs 
	temp = {}
	for key in writable_dirs.keys():
		if ('tracking' in key) == False:
			temp[key] = writable_dirs[key]	
	writable_dirs = temp

def staging():
	# デプロイ対象
	env.deploy_target = "staging"

	env.config_ext = "staging"

	# 設定ファイル読み込み
	_load_conf(env.deploy_target)
	
	# ディレクトリパス
	env.base_dir = "/mnt/Service_code"
	_set_dir_paths()

	# ServiceNameがないので、パスを削除
	global clear_cache_cmds
	clear_cache_cmds = [path for path in clear_cache_cmds if ('ServiceName' in path) == False]
	global check_cache_files
	check_cache_files = [path for path in check_cache_files if ('ServiceName' in path) == False]
	global configs
	configs = [path for path in configs if ('ServiceName' in path) == False]
	global writable_dirs 
	temp = {}
	for key in writable_dirs.keys():
		if ('ServiceName' in key) == False:
			temp[key] = writable_dirs[key]	
	writable_dirs = temp

def _load_conf(type):
	execfile( "../_conf/"+type+".conf" )

def _set_dir_paths():
	env.current_symlink = env.base_dir + "/DocumentRoot"
	env.releases_dir = env.base_dir + "/releases"
	env.app_data_dir = env.base_dir+"/app_data"

# デプロイ実行（ファイル配置まで）
def deploy(tag=""):
	if tag=="" :
		abort("usage fab [option] deploy:tagname")

	print "execute deploy '"+tag+"'"

	# リポジトリをローカルにclone(初回のみ）
# ローカルディスクが全然足りないのでとりあえずあきらめ
#	compress_repository(tag)

	# 圧縮ファイル名
#	repo_filepath = get_repo_filepath(tag)
#	print repo_filepath
	
	# 設置ディレクトリ
	deploy_dir = env.releases_dir+"/"+get_now()+"_"+tag
	print deploy_dir
	
	# リポジトリのファイルを展開
	run(clone_cmd.format(tag=tag, dir=deploy_dir))
	run("rm -rf "+deploy_dir+"/.svn")	# 不要ファイル削除

	# ディレクトリ付け替え
	for dest, src in writable_dirs.items():
		src_dir = env.app_data_dir+"/"+src
		dest_dir = deploy_dir+"/"+dest
		run("rm -rf "+dest_dir)
		run("ln -s {src} {dest}".format(src=src_dir, dest=dest_dir))

	# 設定ファイル変更
	for config in configs:
		config_path = deploy_dir+"/"+config
		#config_path_prod = "./"+os.path.basename(config_path)+"."+env.deploy_target
		config_path_prod = "./"+os.path.basename(config_path)+"."+env.config_ext
		run("rm -rf "+config_path)
		run("ln -s {src} {dest}".format(src=config_path_prod, dest=config_path))
	
	print """next:
	fab [option] commit               -> switch symbolic link current to latest deploy dir
	fab [option] clean                -> remove latest deploy dir"""

def get_now():
	global now_datetime
	if now_datetime == "":
		now_datetime = datetime.datetime.now().strftime(u'%Y%m%d%H%M%S')

	return now_datetime

def get_repo_filepath(tag):
	return "/tmp/"+tag+".tgz"

@runs_once
def compress_repository(tag):
	print "compress repository"
	
	local_clone_dir = "/tmp/"+tag
	if os.path.exists(local_clone_dir):
		local("rm -rf "+local_clone_dir);
	local_compress_file = get_repo_filepath(tag)
	if os.path.exists(local_compress_file):
		local("rm -rf "+local_compress_file);
	# clone
	local(clone_cmd.format(tag=tag, dir=local_clone_dir))	

	# compress
	local("tar cfz --exclude .svn"+local_compress_file+" "+local_clone_dir)

	# clean
	local("rm -rf "+local_clone_dir)

def commit():
	latest_dir = "{0}/{1}".format(env.releases_dir,get_latest_dir())
	print "switch symobic link current to [{0}]".format(latest_dir)
	
	run("rm -rf {0}".format(env.current_symlink))	# remove current symlink
	run("ln -s {0} {1}".format(latest_dir, env.current_symlink))	# make symlink

	# clear cache
	clear_cache()

	print "\n"
	list()

	print """
	fab [option] rollback             -> rollback deploy"""

def clear_cache():
	print "clear CakePHP cache"
	for cmd in clear_cache_cmds:
		sudo(cmd)
	print "clear CakePHP cache done."

def rollback():
	rollback_dir = "{0}/{1}".format(env.releases_dir,get_rollback_dir())
	print "switch symobic link current to [{0}]".format(rollback_dir)
	
	run("rm -rf {0}".format(env.current_symlink))	# remove current symlink
	run("ln -s {0} {1}".format(rollback_dir, env.current_symlink))	# make symlink

	# clear cache
	clear_cache()

	print "\n"
	list()

def clean():
	current_dir = get_current_dir()
	latest_dir = get_latest_dir()

	if current_dir == latest_dir :
		abort("current is lastest !!")
	
	run("rm -rf {0}/{1}".format(env.releases_dir, latest_dir))

	print "\n"
	list()

def list():
	print "current:"
	result = run("ls -l {0}".format(env.current_symlink))

	print "releases:"
	run("ls -lr {0}".format(env.releases_dir))

def get_latest_dir():
	with hide('running', 'stdout', 'stderr'):
		result = run("ls -m -r {0}".format(env.releases_dir))
	latest = result.split(",")[0].strip()
	return latest

def get_rollback_dir():
	with hide('running', 'stdout', 'stderr'):
		result = run("ls -m -r {0}".format(env.releases_dir))
	latest = result.split(",")[1].strip()
	return latest

def get_current_dir():
	with hide('running', 'stdout', 'stderr'):
		result = run("ls -l {0}".format(env.current_symlink))
	return result.split("/")[-1]

def df():
	run("df -h")

def check_cache(keyword=""):
	for file in check_cache_files:
		if exists(file) :
			#run( "php -r 'var_dump(unserialize(file(\""+file+"\")[1]));' | grep "+keyword )
			run( "php -r 'var_dump(unserialize(file(\""+file+"\")[1]));'" )
		else :
			print file+" is not found.\n"
