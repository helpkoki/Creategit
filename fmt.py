import os


class  fileManagerTool:
       
       def __init__(self):
               pass
       
       def read_file_byte(self ,path):
        with open(path, 'rb') as f:
            return f.read()
        
       def read_file(self ,path):
        with open(path, 'rb') as f:
            return f.read()
        
       def repo_find(path=".", required=True):
        path = os.path.realpath(path)

        if os.path.isdir(os.path.join(path, ".git")):
            return path

        # If we haven't returned, recurse in parent, if w
        parent = os.path.realpath(os.path.join(path, ".."))

        if parent == path:
         
            if required:
                raise Exception("No git directory.")
            else:
                return None
   
        # Recurse in the parent directory
        return fileManagerTool.repo_find(parent, required)
       
       #Write data bytes to file at given path.  
       def write_file(path, data):
    
        with open(path, 'wb') as f:
          f.write(data)

      #Compute path under repo's gitdir.
       def repo_path(repo, *path):
        return os.path.join(repo, *path)
       
        #Get current commit hash (SHA-1 string) of local master branch.
       def get_local_master_hash(self):
           master_path = os.path.join('.git', 'refs', 'heads', 'master')
           try:
              return self.read_file_byte(master_path).decode().strip()
           except FileNotFoundError:
             return None