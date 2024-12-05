import hashlib
import os
import zlib
import struct

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
        #  print(sha.hexdigest())
         return sha.hexdigest()
    
    def  hash_object_write(self):
         self.store_object()

    def   create_empty_index(self):
          indexFile = os.path.join(self.gitdir, "index")
        
          #step 1:Create the header 
          signature =b'DIRC'
          version =2
          entries = 0

          # Pack header: <signature (4 bytes), version (4 bytes), entries (4 bytes)>
          header = struct.pack(">4sII", signature, version, entries)
          print(header)
          try:
            with open(indexFile, "wb") as file:
                file.write(header)
          except IOError as e:
            print(f"Error creating index file: {e}")

    def  create_tree(self):
         index_file = os.path.join(self.gitdir, "index")

         if not os.path.exists(index_file):
            print("Index file does not exist.")
            return
         
         entries = []
         with open(index_file ,"r") as f:
              for line in f :
                  print(line)  
 

    def read_index(self):
        indexFile = os.path.join(self.gitdir, "index")
        
        if not os.path.exists(indexFile):
            print("Index file does not exist.")
            return

        with open(indexFile, "rb") as file:
             data = file.read()  # Read binary and decode to string
        
        # Split entries by newline to handle multiple lines
        print("DATA:")
        print(data)
        entries = data.strip().split("\n")
        for entry in entries:
            mode, hash_value, stage, path = entry.split(maxsplit=3)
            print(f"Mode: {mode}, Hash: {hash_value}, Stage: {stage}, Path: {path}")

    
    def  update_index(self):
         indexFile = os.path.join(self.gitdir, "index")
         if  not(os.path.exists(indexFile)):
             self.create_empty_index()
             print("PASSED")

    def  read_byte(self):
         indexFile = os.path.join(self.gitdir, "index")
        
         if not os.path.exists(indexFile):
            print("Index file does not exist.")
            return

         with open(indexFile, "rb") as file:
             data = file.read()

         return data 

    def read_index_header(self):
            indexFile = os.path.join(self.gitdir, "index")
            
            if not os.path.exists(indexFile):
                print("Index file does not exist.")
                return

            with open(indexFile, "rb") as file:
                header = file.read(12)  # Read first 12 bytes

            if len(header) < 12:
                print("Index file is too short.")
                return

            # Unpack header: 4-byte signature, 4-byte version, 4-byte number of entries
            signature, version, num_entries = struct.unpack(">4sII", header)

            signature = signature.decode("ascii")

            # Print parsed data for clarity
            print(f"Signature: {signature}")
            print(f"Version: {version}")
            print(f"Number of entries: {num_entries}")

            return {
                "signature": signature,
                "version": version,
                "num_entries": num_entries
            }
    def read_index_entry(self ,file):
        entry = file.read(62)  # Read the fixed-length part of the entry
        if len(entry) < 62:
            return None  # End of file or corrupted index

        # Unpack the fixed-length data
        ctime, ctime_ns, mtime, mtime_ns, dev, ino, mode, uid, gid, size, sha1, flags = struct.unpack(">10I20sH", entry)

        # Read the variable-length file name
        file_name = b""
        while True:
            byte = file.read(1)
            if byte == b"\x00":  # Null-terminator marks the end of the name
                break
            file_name += byte

        file_name = file_name.decode("utf-8")

        # Align to 8-byte boundary
        padding = (8 - (62 + len(file_name) + 1) % 8) % 8
        file.read(padding)

        return {
            "ctime": ctime,
            "mtime": mtime,
            "dev": dev,
            "ino": ino,
            "mode": mode,
            "uid": uid,
            "gid": gid,
            "size": size,
            "sha1": sha1.hex(),
            "flags": flags,
            "file_name": file_name
        }

    def read_all_entries(self):
        indexFile = os.path.join(self.gitdir, "index")

        if not os.path.exists(indexFile):
            print("Index file does not exist.")
            return []

        entries = []

        # Open the index file and read entries
        with open(indexFile, "rb") as file:
            file.seek(12)  # Skip the 12-byte header

            while True:
                entry =self.read_index_entry(file)
                if entry is None:
                    break  # End of file or no more valid entries
                entries.append(entry)

        return entries