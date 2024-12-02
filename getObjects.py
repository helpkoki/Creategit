import os
import zlib

class GitObject(object):
    def __init__(self, object_hash, force=False):
        self.worktree = os.getcwd()
        self.gitdir = os.path.join(self.worktree, ".git")

        # Ensure we're in a Git repository
        if not (force or os.path.isdir(self.gitdir)):
            raise Exception(f"Not a Git repository: {self.worktree}")

        # Construct the object path
        object_path = os.path.join(self.gitdir, "objects", object_hash[:2], object_hash[2:])

        # Check if the file exists
        if not os.path.isfile(object_path):
            raise Exception("Object does not exist")

        # Save the correct file path
        self.object_path = object_path

    def read_git_object(self):
        """Read and decompress the Git object."""
        with open(self.object_path, "rb") as f:
            compressed_object = f.read()
            return zlib.decompress(compressed_object)

    def parse_object(self, decompressed_data):
        """
        Parse the decompressed Git object to extract its type and content.
        Git objects start with "<type> <size>\0".
        """
        try:
            header, content = decompressed_data.split(b'\x00', 1)
            object_type, _size = header.split(b' ', 1)
            return object_type.decode('utf-8'), content
        except Exception as e:
            raise Exception(f"Failed to parse object: {e}")

    def cat_file_t(self):
        """Display the type of the Git object."""
        decompressed_data = self.read_git_object()
        object_type, _content = self.parse_object(decompressed_data)
        print(object_type)

    def cat_file_p(self):
        """Pretty-print the content of the Git object."""
        decompressed_data = self.read_git_object()
        object_type, content = self.parse_object(decompressed_data)

        if object_type == "blob":
            self.pretty_print_blob(content)
        elif object_type == "tree":
            self.pretty_print_tree(content)
        elif object_type == "commit":
            self.pretty_print_commit(content)
        elif object_type == "tag":
            self.pretty_print_tag(content)
        else:
            raise Exception(f"Unsupported object type: {object_type}")
    
    def parse_tree(self, content):
        """
        Parse and display a tree object.
        Tree objects contain entries in the format:
        <mode> <filename>\0<20-byte SHA-1>
        """
        idx = 0
        while idx < len(content):
            # Parse mode
            space_idx = content.find(b' ', idx)
            mode = content[idx:space_idx].decode('utf-8')

            # Parse filename
            null_idx = content.find(b'\x00', space_idx)
            filename = content[space_idx + 1:null_idx].decode('utf-8')

            # Parse SHA-1
            sha_start = null_idx + 1
            sha_end = sha_start + 20
            sha = content[sha_start:sha_end].hex()

            print(f"{mode} {sha} {filename}")

            # Update index
            idx = sha_end

    def pretty_print_blob(self, content):
        """Print the content of a blob object."""
        print(content.decode('utf-8'))

    def pretty_print_tree(self, content):
        """
        Print the entries of a tree object.
        Tree objects contain entries in the format:
        <mode> <filename>\0<20-byte SHA-1>
        """
        idx = 0
        while idx < len(content):
            space_idx = content.find(b' ', idx)
            mode = content[idx:space_idx].decode('utf-8')

            null_idx = content.find(b'\x00', space_idx)
            filename = content[space_idx + 1:null_idx].decode('utf-8')

            sha_start = null_idx + 1
            sha_end = sha_start + 20
            sha = content[sha_start:sha_end].hex()

            print(f"{mode} {sha} {filename}")
            idx = sha_end

    def pretty_print_commit(self, content):
        """
        Print the metadata and message of a commit object.
        Commit objects are in plain-text format with headers and a message.
        """
        commit_data = content.decode('utf-8')
        print(commit_data)

    def pretty_print_tag(self, content):
         """""
        Print the metadata and message of a tag object.
        Tag objects are similar to commit objects with headers and a message.
        """
         tag_data = content.decode('utf-8')
         print(tag_data)
