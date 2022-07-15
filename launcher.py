import git

repo = git.Repo('~/NEMSELFIE/NemSelfie-Python')
repo.remotes.origin.pull()

import main

main.init()