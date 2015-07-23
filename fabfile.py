__author__ = 'can'

from datetime import datetime

from fabric.operations import run, put, env, local

version_date = datetime.now()
env.version = version_date.strftime("%Y%m%d%H%M")
env.release = env.version


def production():
    env.hosts = ['<server-ip>']

    env.code_root = "/opt/googleplayscraper"
    env.project_name = "googleplayscraper"

    env.releases_path = '%s/releases' % env.code_root
    env.new_release_path = "%s/%s" % (env.releases_path, env.release)

    env.virtualenv_name = "googleplayscraper-py3"


def deploy():
    upload_tar_from_git(env.new_release_path)

    symlink_current_release()

    install_requirements()


def upload_tar_from_git(path):
    file_name = "%s.tgz" % (env.release)
    local('tar cvfz %s .' % (file_name))
    run('mkdir -p %s' % (path))
    run('mkdir -p %s/packages/' % (env.code_root))
    put(file_name, '/tmp', mode="0755")
    run('mv /tmp/%s %s/packages/' % (file_name, env.code_root))

    run('cd %s && tar zxf ../../packages/%s' % (env.new_release_path, file_name))

    local('rm %s' % (file_name))


def symlink_current_release():
    #Symlink our current release
    run('rm %s/current' % (env.code_root))
    run('cd %s;ln -s %s current; chown %s -R current; chgrp %s -R current' % (
        env.code_root, env.new_release_path, env.user, env.user))

def install_requirements():
    run('~/.virtualenvs/%s/bin/pip install -r %s/current/requirements/prod.txt' % (env.virtualenv_name, env.code_root))

def stop():
    run('pkill -f %s' % (env.project_name))

def start():
    run('%s/current/start.sh' % (env.code_root))

