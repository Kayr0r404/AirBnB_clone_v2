#!/usr/bin/python3
# distributes an archive to your web servers, using the function do_deploy
from fabric.api import env, put, run, local
from os.path import exists
env.hosts = ['100.25.136.187', '54.236.50.4']


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract the archive to
        # /data/web_static/releases/<filename without extension>/
        file_name = archive_path.split('/')[-1]
        folder_name = '/data/web_static/releases/{}'.format(
            file_name.split('.')[0])
        run('mkdir -p {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {}'.format(file_name, folder_name))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(file_name))

        run('mv {}/web_static/* {}/'.format(folder_name, folder_name))
        run('rm -rf {}/web_static'.format(folder_name))

        # Delete the symbolic link /data/web_static/current
        run('rm -f /data/web_static/current')

        # Create a new symbolic link
        run('ln -s {} /data/web_static/current'.format(folder_name))

        print("New version deployed!")
        return True

    except Exception as e:
        print(e)
        return False
