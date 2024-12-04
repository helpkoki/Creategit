import os
import hashlib
import struct

class GitRepository:
    def __init__(self, gitdir=".git"):
        self.gitdir = gitdir

    def hash_object(self, data, obj_type="blob"):
        """Hash content as a blob or tree and save it as a Git object."""
        header = f"{obj_type} {len(data)}\0".encode()
        full_data = header + data
        sha1 = hashlib.sha1(full_data).hexdigest()
        
        # Save the object in the .git/objects directory
        obj_dir = os.path.join(self.gitdir, "objects", sha1[:2])
        obj_file = os.path.join(obj_dir, sha1[2:])
        os.makedirs(obj_dir, exist_ok=True)
        with open(obj_file, "wb") as f:
            f.write(full_data)
        
        return sha1

    def create_tree(self):
        """Create a tree object based on the current index file."""
        index_file = os.path.join(self.gitdir, "index")
        
        if not os.path.exists(index_file):
            print("Index file does not exist.")
            return

        entries = []
        with open(index_file, "rb") as f:
        # Read and unpack the header (first 12 bytes)
            header = f.read(12)
            print(header)
            signature, version, num_entries = struct.unpack('!4sII', header)
            
            print(f"Signature: {signature.decode('utf-8')}, Version: {version}, Entries: {num_entries}")

    def create_tree1(self):
        """Create a tree object based on the current index file."""
        index_file = os.path.join(self.gitdir, "index")
        
        if not os.path.exists(index_file):
            print("Index file does not exist.")
            return

        entries = []
        with open(index_file, "r") as f:
            for line in f:
                mode, hash_value, stage, path = line.strip().split(maxsplit=3)
                entry = f"{mode} {hash_value} {path}\n"
                entries.append(entry)

        tree_data = "".join(entries).encode()
        tree_hash = self.hash_object(tree_data, obj_type="tree")
        print(f"Tree created with hash: {tree_hash}")


    def   tree_create(self):
           index_file = os.path.join(self.gitdir, "index")
           if not os.path.exists(index_file):
               return 'Error file does not exist'
           
           
           with open(index_file, 'rb') as f:
                 contact= f.read()
                 size =len(contact)

                
                    
                    