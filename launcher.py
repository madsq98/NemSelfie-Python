import git

repo = git.Repo('/home/pi/NEMSELFIE/nemselfie-python')
repo.remotes.origin.pull()

import main

main.init()