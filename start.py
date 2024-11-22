import os
import sys
import argparse
from getInit import getInit  # Make sure gitInit.py is in the same directory or in your Python path
from getObjects import GitObject
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
argsp.add_argument(
                        "-t",
                        action="store_true",
                        help="Show the type of the Git object.",
                    )
argsp.add_argument(
                    "-p",
                    action="store_true",
                    help="Print the content of the Git object.",
                )

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
     git_obj =GitObject(args.sha1 )
     if  args.t :
         git_obj.cat_file_t()
     elif args.p :
             git_obj.cat_file_p()  
     elif args.p and args.t:
          print("please choose one between -p and -t")
     else:
          print('Error incorrect run startment  ')

    #  git_obj =GitObject(args.sha1 )
    #  git_obj.cat_file_t()
    #  git_obj.cat_file_p()