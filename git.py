import argparse
import collections
import configparser
from datetime import datetime
import grp, pwd
from fnmatch import fnmatch
import hashlib
from math import ceil
import os
import re
import sys
import zlib


class GitRepository (object):
    """A git repository"""

    worktree = None
    gitdir = None
    conf = None

    def __init__(self, path, force=False):
       self.worktree =path
       self.gitdir =os.path.join(self.worktree ,'.git')
      
       print(self.worktree)  
       print(self.gitdir)

       if not (force or os.path.isdir(self.gitdir)):
           raise Exception("Not a git repository: %s" % self.worktree)
       
       self.conf =configparser.ConfigParser()
       cf =self.repo_file(self ,'config')
       print(cf)


    def repo_path(repo, *path):
    # """Compute path under repo's gitdir."""
     return os.path.join(repo.gitdir, *path)
    
    
    def repo_file(repo, *path, mkdir=False):
        #     """Same as repo_path, but create dirname(*path) if absent.  For
        # example, repo_file(r, \"refs\", \"remotes\", \"origin\", \"HEAD\") will create
        # .git/refs/remotes/origin."""

     if repo_dir(repo, *path[:-1], mkdir=mkdir):
        return repo_path(repo, *path)

def repo_dir(repo, *path, mkdir=False):
    """Same as repo_path, but mkdir *path if absent if mkdir."""

    path = repo_path(repo, *path)

    if os.path.exists(path):
        if (os.path.isdir(path)):
            return path
        else:
            raise Exception("Not a directory %s" % path)

    if mkdir:
        os.makedirs(path)
        return path
    else:
        return None