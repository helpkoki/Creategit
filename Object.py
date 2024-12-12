import os 
import zlib
import hashlib
import struct


class GitObject:

    def __init__(self):
        self.worktree = os.getcwd()

    def hash_object(self ,data , object_type , write= True):
         # Ensure data is in bytes
        if isinstance(data, str):
           print("RIN")
           data = data.encode('utf-8')  # Convert string to bytes if necessary
        

        size = len(data)  # Calculate size in bytes
        wrapped = bytes(f"{object_type} {size}\0", 'utf-8') + data
        sha1 = hashlib.sha1(wrapped).hexdigest()

        if write:
            path =os.path.join('.git','objects', sha1[:2], sha1[2:]) 
            if not os.path.exists(path):
             a= os.makedirs(os.path.dirname(path),exist_ok=True)
             self.write_file(path ,zlib.compress(wrapped))

        return  wrapped     

       # Write data bytes to file at given path.
    def write_file(self ,path, data):
        with open(path, 'wb') as f:
            f.write(data) 
     #Read contents of file at given path as bytes.
    def read_file(self ,path):
        with open(path, 'rb') as f:
            return f.read()