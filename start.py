import os
import sys
import argparse
from getInit import getInit  # Make sure gitInit.py is in the same directory or in your Python path
from getObjects import GitObject
from setObject import Object
from GitRepository import GitRepository
from add import one
from read import GitIndexReader
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
argsp.add_argument(   "-t",
                        action="store_true",
                        help="Show the type of the Git object.",
                    )
argsp.add_argument(  "-p",
                    action="store_true",
                    help="Print the content of the Git object.",
                  )
argsp.add_argument("sha1", 
                    metavar="sha1",
                    help="The SHA-1 hash of the object to examine.")
#the hash-object command
argsp = argsubparsers.add_parser(
    "hash-object",
    help="Compute object ID and optionally creates a blob from a file")

argsp.add_argument("-t",
                   metavar="type",
                   dest="type",
                   choices=["blob", "commit", "tag", "tree"],
                   default="blob",
                   help="Specify the type")

argsp.add_argument("-w",
                    dest="write",
                    action="store_true",
                    help="Actually write the object into the database")

argsp.add_argument("path",
                    help="Read object from <file>")

argsp = argsubparsers.add_parser(
        "update-index",
        help="it updates the index used for `add` and `commit` commands")

argsp.add_argument("path",
                   help="Read object from <file>")

argsp = argsubparsers.add_parser(
    "write-tree",
    help="Compute object ID and optionally creates a blob from a file")
argsp = argsubparsers.add_parser(
                                  "test",
                                   help="it updates the index used for `add` and `commit` commands")

def  main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)
    match args.command:
        case "init"         : get_init(args)
        case "cat-file"     : get_cat_file(args)
        case "hash-object"  : get_hash_object(args)
        case "update-index" : get_update_index(args)
        case "write-tree"   : get_write_tree(args)
        case "test"         : test(args)
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

def get_hash_object(args):
    y = Object(args.path)
    print(args)
    if not(args.write):
        # y.hash_object()
         y.update_index()
    else:
       y.hash_object_write()   

def get_update_index(args):
    print(args)
    # print(args.path)
    # path =os.path.join(os.getcwd(),".git" ,"index")
    # print(path)
    # print(os.path.exists(path))

    # y =Object(args.path)
    # # repo = one() # Initialize the repository
    # # repo.update_index(args.path)  
    # y.update_index()
    # y.read_index()

def test(args):
    print("TEST CASE")
   
    index_file_path = '.git/index'  # Path to the Git index file
    # git_index_reader = GitIndexReader(index_file_path)
    # git_index_reader.display_index_data()

    y=Object(index_file_path)
    w = y.read_byte()
    x=y.read_index_header()
    print(x)
    

    print()

    h =y.read_all_entries()
    print(h)
    # entries = [
    #     {
    #          "ctime_ns": 0,
    #         "mtime": 1690000100,
    #         "mtime_ns": 0,
    #         "dev": 16777220,
    #         "ino": 123456,
    #         "mode": 0o100644,
    #         "uid": 1000,
    #         "gid": 1000,
    #         "size": 12345,
    #         "sha1": "d3b07384d113edec49eaa6238ad5ff00",
    #         "file_name": "example.txt"
    #     },
    #     {
    #         "ctime": 1690000200,
    #         "ctime_ns": 0,
    #         "mtime": 1690000300,
    #         "mtime_ns": 0,
    #         "dev": 16777220,
    #         "ino": 654321,
    #         "mode": 0o100755,
    #         "uid": 1000,
    #         "gid": 1000,
    #         "size": 54321,
    #         "sha1": "a9b9f04336ce0181a08e774e01113b31",
    #         "file_name": "script.sh"
    #     }
    # ]

    # h =y.create_index(entries)




def  get_write_tree(args):
     print(args)
     git ='.'
     y =GitRepository()
     y.create_tree1()
        