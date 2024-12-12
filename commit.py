import hashlib
import os
import zlib
import struct

class Object:
      
    

    def __init__(self, file):
        self.worktree = os.getcwd()
        self.gitdir = os.path.join(self.worktree, ".git")
        self.tohash = os.path.join(self.worktree, file)
        self.indexFile = os.path.join(self.gitdir, "index")

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

    def  create_tree(self):
         index_file = os.path.join(self.gitdir, "index")

         entries = self.read_all_entries()  # Read all index entries
         if not entries:
            print("No entries in the index to create a tree.")
            return None

         tree_content = b""
        
            # Format each entry: <file_mode> <file_name>\0<hash>
         for entry in entries:
                mode = f"{entry['mode']:o}"  # Convert mode to octal string
                file_name = entry["file_name"]
                sha1 = bytes.fromhex(entry["sha1"])
                tree_content += f"{mode} {file_name}\0".encode("utf-8") + sha1

            # Prepend header: "tree <size>\0"
         tree_object = f"tree {len(tree_content)}\0".encode("utf-8") + tree_content

            # Hash and store the tree object
         sha = hashlib.sha1(tree_object).hexdigest()
         dir_path = os.path.join(self.gitdir, "objects", sha[:2])
         file_path = os.path.join(dir_path, sha[2:])
         os.makedirs(dir_path, exist_ok=True)

         with open(file_path, "wb") as f:
            f.write(zlib.compress(tree_object))

         print(f"Tree object created: {sha}")
         return sha 
 

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
    
    def create_index_file(self ,addfile):     
        #step 1:Create the header 
        signature =b'DIRC'.necode("ascii")
        version =2
        entries = 1     



        if not os.path.exists(self.indexFile):
            with open(self.indexFile,"wb") as file:
                  header =struct.pack(">4sII", signature, version, entries)
                  file.write(header) 
        print(header)
        
    def create_index(self, entries):
   
        indexFile = os.path.join(self.gitdir, "index")

        with open(indexFile, "wb") as file:
            # Step 1: Write the header
            signature = b"DIRC"  # 4-byte signature
            version = 2  # 4-byte version number
            num_entries = len(entries)  # 4-byte number of entries

            header = struct.pack(">4sII", signature, version, num_entries)
            file.write(header)

            # Step 2: Write each entry
            for entry in entries:
                # Fixed-length fields (62 bytes)
                ctime = entry.get("ctime", 0)
                ctime_ns = entry.get("ctime_ns", 0)
                mtime = entry.get("mtime", 0)
                mtime_ns = entry.get("mtime_ns", 0)
                dev = entry.get("dev", 0)
                ino = entry.get("ino", 0)
                mode = entry.get("mode", 0o100644)  # Default: regular file with 644 permissions
                uid = entry.get("uid", 0)
                gid = entry.get("gid", 0)
                size = entry.get("size", 0)
                sha1 = bytes.fromhex(entry.get("sha1", "0" * 40))  # SHA-1 as 20 bytes
                flags = len(entry.get("file_name", ""))  # File name length as flags

                # Pack fixed-length fields
                fixed_part = struct.pack(">10I20sH", ctime, ctime_ns, mtime, mtime_ns,
                                        dev, ino, mode, uid, gid, size, sha1, flags)

                file.write(fixed_part)

                # Variable-length field: file name
                file_name = entry["file_name"].encode("utf-8")
                file.write(file_name + b"\x00")  # Null-terminated

                # Align to 8-byte boundary
                entry_length = 62 + len(file_name) + 1  # Fixed part + file name + null byte
                padding = (8 - (entry_length % 8)) % 8
                file.write(b"\x00" * padding)
                print(f"Index file created at {indexFile}")



    def create_entry(file_path, repo_root):
            """
            Create an entry dictionary for the Git index file.

            Parameters:
            - file_path: Full path to the file.
            - repo_root: Root directory of the repository.

            Returns:
            - Dictionary representing the entry.
            """
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"{file_path} does not exist")

            # File stats
            stats = os.stat(file_path)
            
            # Compute SHA-1 hash of file contents
            with open(file_path, "rb") as f:
                file_contents = f.read()
                sha1 = hashlib.sha1(file_contents).hexdigest()

            # File name relative to repo root
            file_name = os.path.relpath(file_path, repo_root)

            # Create entry dictionary
            entry = {
                "ctime": int(stats.st_ctime),            # Last status change time (seconds)
                "ctime_ns": int((stats.st_ctime % 1) * 1e9),  # Nanoseconds part
                "mtime": int(stats.st_mtime),            # Last modification time (seconds)
                "mtime_ns": int((stats.st_mtime % 1) * 1e9),  # Nanoseconds part
                "dev": stats.st_dev,                    # Device number
                "ino": stats.st_ino,                    # Inode number
                "mode": stats.st_mode,                  # File mode (permissions)
                "uid": stats.st_uid,                    # User ID
                "gid": stats.st_gid,                    # Group ID
                "size": stats.st_size,                  # File size in bytes
                "sha1": sha1,                           # SHA-1 hash
                "file_name": file_name                  # Relative file name
            }

            return entry
    
    def add_to_index_entry( self,file_path ,repo_root):
        entry = self.create_entry(file_path, repo_root)
        self.index.append(entry)
