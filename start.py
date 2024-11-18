import os
import sys
from getInit import getInit  # Make sure my_git.py is in the same directory or in your Python path

# Initialize the repository in the current working directory



def  main(argv=sys.argv[1:]):
    try:
        x = getInit(os.getcwd())
    except Exception as e:
        print(e)
