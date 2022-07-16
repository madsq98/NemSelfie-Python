import git
import os
import selfieOptions
from time import sleep
import subprocess
import ftplib

try:
    import httplib  # python < 3.0
except:
    import http.client as httplib


def have_internet():
    conn = httplib.HTTPSConnection("8.8.8.8", timeout=5)
    try:
        conn.request("HEAD", "/")
        return True
    except Exception:
        return False
    finally:
        conn.close()


def git_update():
    print("Updating software...")
    os.environ['GIT_USERNAME'] = "madsq98"
    os.environ['GIT_PASSWORD'] = "yuyatrA48a"
    repo = git.Repo(selfieOptions.HOME_LOCATION)
    repo.remotes.origin.pull()


def upload_pictures():
    res = []

    for path in os.listdir(selfieOptions.PICTURES_LOCATION):
        fullPath = os.path.join(selfieOptions.PICTURES_LOCATION, path)
        if os.path.isfile(fullPath):
            res.append(path)

    session = ftplib.FTP('linux111.unoeuro.com', 'qvistgaard.me', 'FRGka5Dmencr')
    session.cwd('nemselfie')
    session.cwd('uploads')
    for pictureUrl in res:
        fullPath = os.path.join(selfieOptions.PICTURES_LOCATION, pictureUrl)
        print("Uploading " + fullPath)
        print("File size: " + str(os.path.getsize(fullPath) / 1000) + "kb")
        file = open(fullPath, 'rb')
        session.storbinary('STOR ' + pictureUrl, file)
        file.close()
        os.remove(fullPath)

    session.close()


if have_internet():
    git_update()
    upload_pictures()


import main

main.init()
