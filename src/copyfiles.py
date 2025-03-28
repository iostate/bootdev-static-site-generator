# Write a recursive function that copies all the contents from a source directory to a destination directory (in our case, static to public)
# It should first delete all the contents of the destination directory (public) to ensure that the copy is clean.
# It should copy all files and subdirectories, nested files, etc.
# I recommend logging the path of each file you copy, so you can see what's happening as you run and debug your code.

import os
import shutil

def copy_files_recursive(source, destination):
    delete_all_content(destination) # ensures clean copy
    if not os.path.exists(source):
        raise ValueError("source does not exist")
    
    # Create directory if it does not exist
    if not os.path.exists(destination):
        os.makedirs(destination)
        
    
    list_dir = os.listdir(source)
    for filename in list_dir:
        src_path = os.path.join(source, filename)
        dest_path = os.path.join(destination, filename)
        if os.path.isdir(src_path):
            copy_files_recursive(src_path, dest_path)
        else:
            print(f"Copying....\nFrom:\n{src_path} \n->\nTo:\n{dest_path}")
            shutil.copy2(src_path, dest_path)

def delete_all_content(folder):
    if not os.path.exists(folder):
        raise ValueError("folder to delete does not exist")
    list_dir = os.listdir(folder)
    
    for filename in list_dir:
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    