import os
from git import getInit  # Make sure my_git.py is in the same directory or in your Python path

# Initialize the repository in the current working directory


try:
    x = getInit(os.getcwd())
except Exception as e:
    print(e)
