import os

class getInit(object):
    worktree = None
    getdir = None

    def __init__(self, path):
        self.worktree = path
        self.getdir = os.path.join(path, '.git')
        # Check if Git repository (.git) exists than act accouding
        self.check_repo()

    # Check if Git repository (.git) exists
    def check_repo(self):
        if os.path.exists(self.getdir):
            raise Exception('Git directory already exists. Reinitialize the Git repository.')
        else:
            self.create_repo()

    def create_repo(self):
        try:
            # Create the .git directory and its subdirectories in the specified worktree path
            os.mkdir(self.getdir)
            os.mkdir(os.path.join(self.getdir, "objects"))
            os.mkdir(os.path.join(self.getdir, "refs"))
            
            # Create the HEAD file with a reference to the main branch
            head_path = os.path.join(self.getdir, "HEAD")
            with open(head_path, "w") as f:
                f.write("ref: refs/heads/main\n")
            
            print(f"Initialized empty Git repository in {self.getdir}")

        except FileExistsError:
            print("Git directory already exists. No need to reinitialize.")
        except Exception as e:
            print(f"Error during repository initialization: {e}")