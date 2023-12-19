#!/usr/bin/python3
""" Fabric script that creates and distributes an archive to your web servers,
using the function deploy. """
import os
from fabric.api import *
from datetime import datetime

env.hosts = ['54.210.173.123', '54.175.145.44']


def do_pack():
    """ Generates a .tgz archive from the contents of the
    web_static directory. """
    # Create the folder versions if not exists
    local("mkdir -p versions")
    # Create the file with date format
    date = datetime.now()
    date_format = date.strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date_format)
    # Compress file
    try:
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
        return None


def do_deploy(archive_path):
    """ Distributes an archive to your web servers. """
    if not os.path.exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        file_name_no_ext = file_name.split(".")[0]
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p /data/web_static/releases/{}/".format(file_name_no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(file_name, file_name_no_ext))
        run("rm /tmp/{}".format(file_name))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/"
            .format(file_name_no_ext, file_name_no_ext))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(file_name_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(file_name_no_ext))
        return True
    except Exception:
        return False


def deploy():
    """ Creates and distributes an archive to your web servers. """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
