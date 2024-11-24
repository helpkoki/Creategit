import hashlib
import os

class setObject(object):
      
      def  __init__(self, file ):
           self.worktree = os.getcwd()
           self.gitdir = os.path.join(self.worktree, ".git")
           self.tohash =  os.path.join(self.gitdir ,file)
              # Ensure we're in a Git repository
           if not ( os.path.isdir(self.gitdir)):
              raise Exception(f"Not a Git repository: {self.worktree}")
               # Construct the object path
           if not( os.path.isfile(self.gitdir(self.tohash))):
              raise Exception(f"could not open: {self.worktree} for reading: No such file or directory")

      def wrap_file(file_path):
        with open(file_path, 'r') as f:
          content = f.read()
          size = len(content)  # Calculate size in bytes
          wrapped = f"blob {size}\0{content}".encode('utf-8')
          return wrapped
          

       
            
     
       