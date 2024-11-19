import os
import sys
import argparse
from getInit import getInit  # Make sure gitInit.py is in the same directory or in your Python path
from getObjects import getObjects
# Initialize the repository in the current working directory

argparser = argparse.ArgumentParser(description="The stupidest content tracker")

argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True

# `init` command
argsp = argsubparsers.add_parser("init", help="Initialize a new, empty repository.")
argsp.add_argument("path",
                    metavar="directory", 
                    nargs="?",
                    default=".", 
                    help="Where to create the repository.")

# `cat-file` command
argsp = argsubparsers.add_parser("cat-file",
                                  help="Provide the object referred to by SHA-1")
argsp.add_argument("sha1", 
                    metavar="sha1",
                    help="The SHA-1 hash of the object to examine.")



def  main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)
    match args.command:
        case "init"         : get_init(args)
        case "cat-file"     : get_cat_file(args)
        case _              : print("Bad command.")
     
    print()
    
def  get_init(args):
    try: 
        # print(args.command)
        # print(args)
        # print(type(args))
        x = getInit(args.path)
    except Exception as e:
        print("ERROR")
        print(e)

def  get_cat_file(args):
     print(args)
     x =getObjects()