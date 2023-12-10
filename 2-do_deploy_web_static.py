#!/usr/bin/python3
from fabric.api import *
env.hosts = ['100.25.136.187', '54.236.50.4']


def do_deploy(archive_path):
    # env.user = 'ubuntu'
    # env.key_filename = [' ~/.ssh/id_rsa']
    try:
        # upload archieve to /tmp
        put(archive_path, '/tmp/')
        archive_name = archive_path.split('/')[-(
            len(archive_path.split('/')) - 1)].split('.')[0]
        run('mkdir -p /data/web_static/releases/{}'.format(archive_name))
        # uncompress the archive
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}'.format(
            archive_name, archive_name))
        # remove the archieve
        run("rm /tmp/{}.tgz".format(archive_name))
        # remove
        run('rm -rf /data/web_static/current')
        # create a new link
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.
            format(archive_name))
        return True
    except Exception as e:
        # failure to locate archive file
        return False
