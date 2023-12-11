#!/usr/bin/python3
# deletes out-of-date archives, using the function do_clean

from fabric.api import *
import os
env.hosts = ['100.25.136.187', '54.236.50.4']
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_clean(number=0):
    '''Deletes outdated archives on the local machine
    and remote servers
    number is the number of the archives, including the most recent, to keep'''
    number = 1 if int(number) < 1 else int(number)
    # remove old archives on local
    local_archives = sorted(os.listdir("versions"))

    for i in range(len(local_archives) - number):
        local('rm versions/{}'.format(local_archives[i]))

    # remove old archives on remote servers
    path_name = '/data/web_static/releases'
    server_archives = sorted(run('ls {}'.format(path_name)).split())
    del server_archives[0]
    for i in range(len(server_archives) - number):
        run('rm -r {}/{}'.format(path_name, server_archives[i]))
