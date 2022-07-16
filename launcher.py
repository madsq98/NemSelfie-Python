import git
import os
import selfieOptions
from time import sleep
import subprocess

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
    os.environ['GIT_USERNAME'] = "madsq98"
    os.environ['GIT_PASSWORD'] = "yuyatrA48a"
    repo = git.Repo(selfieOptions.HOME_LOCATION)
    repo.remotes.origin.pull()


def upload_pictures():
    res = []

    for path in os.listdir(selfieOptions.PICTURES_LOCATION):
        if os.path.isfile(os.path.join(selfieOptions.PICTURES_LOCATION, path)):
            res.append(path)

    for pictureUrl in res:
        print("Uploading " + pictureUrl)
        os.remove(pictureUrl)
        sleep(2)


if have_internet():
    upload_pictures()
    git_update()

import main

main.init()
