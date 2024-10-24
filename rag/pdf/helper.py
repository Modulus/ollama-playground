import os

def get_root_folder():

    # get current directory
    path = os.getcwd()
    print("Current Directory", path)

    
    # prints parent directory
    path = os.path.abspath(os.path.join(path, os.pardir, os.pardir))
    print("Root folder", path)
    return path
