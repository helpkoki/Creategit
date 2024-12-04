import hashlib
import os
import zlib
import struct

class one:
    def __init__(self, repo_path=".git"):
        """Initialize the Git repository."""
        self.repo_path = repo_path
        self.objects_path = os.path.join(repo_path, "objects")
        if not os.path.exists(self.objects_path):
            os.makedirs(self.objects_path, exist_ok=True)
        print(f"Initialized repository at {self.repo_path}")

    def hash_file(self, file_path):
        """Compute the Git-style hash of a file and prepare its storage content."""
        with open(file_path, 'rb') as f:
            content = f.read()
        
        # Create Git blob header: "blob {size}\0"
        header = f"blob {len(content)}\0".encode()
        store = header + content
        
        # Compute SHA-1 hash
        sha1 = hashlib.sha1(store).hexdigest()
        return sha1, store

    def write_object(self, sha1, store):
        """Write the object to the .git/objects directory."""
        obj_dir = os.path.join(self.objects_path, sha1[:2])
        obj_file = os.path.join(obj_dir, sha1[2:])
        
        os.makedirs(obj_dir, exist_ok=True)
        
        # Compress the content (Git uses zlib compression)
        compressed_data = zlib.compress(store)
        
        with open(obj_file, 'wb') as f:
            f.write(compressed_data)
        
        print(f"Object stored at {obj_file}")

    def add(self, file_path):
        """Simulate the `git add` command."""
        if not os.path.isfile(file_path):
            print(f"Error: {file_path} does not exist or is not a file.")
            return
        
        sha1, store = self.hash_file(file_path)
        self.write_object(sha1, store)
        print(f"File '{file_path}' added with SHA-1: {sha1}")

    def update_index(self, file_path):
        """Update the Git index with the given file."""
        sha1, _ = self.hash_file(file_path)
        stat = os.stat(file_path)

        # Ensure SHA-1 is exactly 20 bytes (it should already be, but we need to confirm)
        sha1_bytes = bytes.fromhex(sha1)
        if len(sha1_bytes) != 20:
            raise ValueError(f"Invalid SHA-1 length: {len(sha1_bytes)} bytes, expected 20 bytes")

        # Prepare index entry
        path_len = len(file_path.encode()) + 1  # Null-terminated string (+1 for \0)
        entry = struct.pack(
            '>IIIIIIII20sH',  # Struct format for 10 items
            int(stat.st_ctime),              # Creation time (seconds)
            int(stat.st_ctime_ns % 1e9),     # Creation time (nanoseconds)
            int(stat.st_mtime),              # Modification time (seconds)
            int(stat.st_mtime_ns % 1e9),     # Modification time (nanoseconds)
            stat.st_dev,                     # Device ID
            stat.st_ino,                     # Inode number
            stat.st_mode,                    # Mode (permissions)
            stat.st_uid,                     # User ID
            stat.st_gid,                     # Group ID
            sha1_bytes,                      # SHA-1 hash (20 bytes)
            path_len                         # Path length
        ) + file_path.encode() + b'\0'       # File path with null terminator

        # Write the index header + entry
        with open(".git/index", "wb") as f:
            f.write(struct.pack(">4sII", b'DIRC', 2, 1))  # Header: "DIRC" + version 2 + 1 entry count
            f.write(entry)

        print(f"Updated index with {file_path}")