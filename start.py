import argparse , collections ,os , zlib
from repo import Repository
from index import Index
from commit import Object
from Object import GitObject
from fmt import fileManagerTool


def main():
     argparser = argparse.ArgumentParser(description="The stupidest content tracker")

     sub_parser = argparser.add_subparsers(title="Command", dest="command")
     sub_parser.required = True 

     init_parser = sub_parser.add_parser('init', help='initialize a new repository')
     init_parser.add_argument('repo_path',
                               metavar='repo_path',
                               nargs="?",
                               default=".",
                               help='path to initialize the repository')


     add_parser =sub_parser.add_parser('add', help='add file(s) to the index file')
     add_parser.add_argument('paths' , nargs='+' ,metavar='path' ,
                             help='path(s) of files to add ')
     

     add_parser =sub_parser.add_parser('tree', help='it create a tree from the index')


     sub_parser = sub_parser.add_parser(
                                  "test",
                                   help="it updates the index used for `add` and `commit` commands")

       
     args = argparser.parse_args()

     match args.command:
          case 'init'        : init(args)
          case  'tree'       : tree(args)
          case  'test'       : test(args)
          case _             : print("Bad command.") 
        



def  init(args):
      x = Repository()
      x.init(args.repo_path)

def  test(args):
     x =Index()
     # print(x.write_tree()) 
     x.commit('jeioiwi' ,None)
     y =fileManagerTool() 
     print(os.getcwd())
     
def tree(args):
     print("tree")
     x =Index()
     # print(x.write_tree()) 
     x.commit('jeioiwi' ,None)
     y =fileManagerTool() 
     print(os.getcwd())
     