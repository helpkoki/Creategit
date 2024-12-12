import collections ,struct
import os , hashlib
from fmt import fileManagerTool
from Object import GitObject
class Index:

    def __init__(self):
        self.fmt =fileManagerTool()
        self.gitObj =GitObject()
        self.IndexEntry = collections.namedtuple('IndexEntry', [
            'ctime_s', 'ctime_n', 'mtime_s', 'mtime_n', 'dev', 'ino', 'mode',
            'uid', 'gid', 'size', 'sha1', 'flags', 'path',
        ])

       
    def read_index(self):
        
        try:
            data =self.fmt.read_file(os.path.join('.git', 'index'))

            digest = hashlib.sha1(data[:-20]).digest() #the index checksum
            assert digest == data[-20:]#check the index checksum
            signature , version , num_entries = struct.unpack('>4sLL' , data[:12])
            assert signature == b'DIRC' , 'invalid index signature {}'.format(signature)
            assert version == 2, 'unknown index version {}'.format(version)
            #extracts a slice of data starting from the 13th element and ending 20 elements before the end
            entry_data = data[12:-20]
            entries = []
            i = 0
         
            while i + 62 < len(entry_data):
                 fields_end = i + 62
                 fields = struct.unpack('!LLLLLLLLLL20sH', entry_data[i:fields_end])
                 
                 path_end = entry_data.index(b'\x00',fields_end)
                 path = entry_data[fields_end:path_end]
                 entry = self.IndexEntry(*(fields + (path.decode(),)))
                 entries.append(entry)
                 entry_len = ((62 + len(path) + 8) // 8) * 8
                 i += entry_len
                
            assert len(entries) == num_entries ,' number  of entries donot macth  files says: {}  seeing :{}'.format( num_entries,len(entries))
            return entries
             
        except FileNotFoundError:
           return []

    #Write a tree object from the current index entries.  
    def write_tree(self):
         tree_entries = []
         for entry in self.read_index():
              assert '/' not in entry.path, \
                'currently only supports a single, top-level directory'
              
              mode_path = '{:o} {}'.format(entry.mode, entry.path).encode()
              tree_entry = mode_path + b'\x00' + entry.sha1
           
              tree_entries.append(tree_entry)

                 
         return self.gitObj.hash_object(b''.join(tree_entries) , 'tree')


    #Commit the current state of the index to master with given message.
    # Return hash of commit object
    def commit(self ,message, author):
        tree =self.write_tree()
        parent = self.fmt.get_local_master_hash()
        if author is None:
            author ='{} <{}>'.format(os.environ['GIT_AUTHOR_NAME'], os.environ['GIT_AUTHOR_EMAIL'])
            print(author)
   
    def read_all_entries(self):
        indexFile = os.path.join(".git" , "index")
                   
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
 
    

