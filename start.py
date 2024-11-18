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
from git import GitRepository

argparser = argparse.ArgumentParser(description="The stupidest content tracker")
argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True
init_parser = argsubparsers.add_parser("init", help="Initialize a new repository")

init_parser.add_argument("path",
                   metavar="directory",
                   nargs="?",
                   default=".",
                   help="Where to create the repository.")

def main(argv=sys.argv[1:]):

   
    args = argparser.parse_args(argv)
    # print('test one two')
    match args.command:
        case "add"          : cmd_add(args)
        case "cat-file"     : cmd_cat_file(args)
        case "check-ignore" : cmd_check_ignore(args)
        case "checkout"     : cmd_checkout(args)
        case "commit"       : cmd_commit(args)
        case "hash-object"  : cmd_hash_object(args)
        case "init"         : cmd_init(args)
        # case "log"          : cmd_log(args)
        # case "ls-files"     : cmd_ls_files(args)
        # case "ls-tree"      : cmd_ls_tree(args)
        # case "rev-parse"    : cmd_rev_parse(args)
        # case "rm"           : cmd_rm(args)
        # case "show-ref"     : cmd_show_ref(args)
        # case "status"       : cmd_status(args)
        # case "tag"          : cmd_tag(args)
        case _              : print("Bad command.")



def cmd_add(args):
    print("Adding files to index...")  # Placeholder

def cmd_init(args):
    repo = GitRepository(args.path ,True)
    # repo.repo_create(args.path)
    print("Initializing repository...")  # Placeholder

def cmd_cat_file(args):
    print("Displaying file contents...")  # Placeholder

def cmd_check_ignore(args):
    print("Checking ignore files...")  # Placeholder

def cmd_checkout(args):
    print("Checking out files...")  # Placeholder

def cmd_hash_object(args):
    print("Hashing object...")  # Placeholder

def cmd_commit(args):
    print("Committing changes...")  # Placeholder
