#!/usr/bin/python3
# creates and distributes an archive to your web servers

from fabric.api import *
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
env.hosts = ['100.25.136.187', '54.236.50.4']
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()

    if not archive_path:
        return False

    return do_deploy(archive_path)
