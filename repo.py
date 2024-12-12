
import os


class Repository:

    
    def __init__(self):
        self.worktree = os.getcwd()
        

    def init(self ,repo):
        # the a two ways to make a git repo one is with in an existing dir and other is to create 
        # a new dir and then make a git repo in it
         # Check if the repository path is the current directory
        if repo == ".":
            repo_path = os.getcwd()  # Use the current working directory
        else:
            repo_path = os.path.abspath(repo)
            # Check if the directory exists; create it if it doesn't
            if not os.path.exists(repo_path):
                    os.mkdir(repo)  # Create the directory if it doesn't exist
            

        try:
            # Create the `.git` directory and its necessary subdirectories
            gitdir = os.path.join(repo_path, ".git")
            if os.path.exists(gitdir):
                print("Git directory already exists. No need to reinitialize.")
                return
            os.mkdir(gitdir)
            os.mkdir(os.path.join(gitdir, "objects"))
            os.mkdir(os.path.join(gitdir, "refs"))

            # Create the `HEAD` file
            head_path = os.path.join(gitdir, "HEAD")
            with open(head_path, "w") as f:
                f.write("ref: refs/heads/master\n")

            print(f"Initialized empty Git repository in {gitdir}")

        except FileExistsError:
            print("Git directory already exists. No need to reinitialize.")
        except Exception as e:
            print(f"Error during repository initialization: {e}")


    