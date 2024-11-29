import hashlib
import os
import zlib

class Object:
    def __init__(self, file):
        self.worktree = os.getcwd()
        self.gitdir = os.path.join(self.worktree, ".git")
        self.tohash = os.path.join(self.worktree, file)

        # Ensure we're in a Git repository
        if not os.path.isdir(self.gitdir):
            raise Exception(f"Not a Git repository: {self.worktree}")

        # Ensure the file to hash exists
        if not os.path.isfile(self.tohash):
            raise Exception(f"Could not open: {self.tohash} for reading: No such file or directory")

    def wrap_file(self, file_path):
        """Read the file content and prepare it for hashing."""
        with open(file_path, 'r') as f:
            content = f.read()
            size = len(content)  # Calculate size in bytes
            wrapped = f"blob {size}\0{content}".encode('utf-8')
            return wrapped

    def store_object(self): 
        """Hash the file, compress its content, and store it in the .git/objects directory."""
        wrap = self.wrap_file(self.tohash)

        # Calculate the hash of the file's content
        sha = hashlib.sha1()
        sha.update(wrap)
        hash_hex = sha.hexdigest()
        print(hash_hex)
        print("about to save the git object")

        # Create the path for storing the object
        dir_path = os.path.join(self.gitdir, "objects", hash_hex[:2])
        file_path = os.path.join(dir_path, hash_hex[2:])

        # Create directory if it doesn't exist
        os.makedirs(dir_path, exist_ok=True)

        # Compress the object
        zi_object = zlib.compress(wrap)

        # Write the compressed object to disk
        with open(file_path, 'wb') as w:
            w.write(zi_object)

        print(f"Object stored: {file_path}")

    def  hash_object(self):
         sha = hashlib.sha1()
         sha.update(self.wrap_file(self.tohash))
         print(sha.hexdigest())
         return sha.hexdigest()
    
    def  hash_object_write(self):
         self.store_object()