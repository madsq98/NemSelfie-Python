import git
import os

os.environ['GIT_USERNAME'] = "madsq98"
os.environ['GIT_PASSWORD'] = "yuyatrA48a"
repo = git.Repo('/home/pi/NEMSELFIE/nemselfie-python')
repo.remotes.origin.pull()

import main

main.init()