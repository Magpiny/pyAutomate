import os
import shutil

# ITERATING OVER THE FILES IN THIS IN THIS FOLDER
for folders, subfolders, filenames in os.walk('/home/magpiny/Documents/Devs/Python/Projects/pyAutomate'):
    print(f"The folder is {folders}")
    print(f"The subfolders in {folders} are {subfolders}")
    print(f"The filenames in {folders} are {filenames}")
    print()

"""
    for subfolder in subfolders:
        if fish in subfolders:
            os.rmdir(subfolder)

    for file in filenames:
        if file.endswith('.py'):
            shutil.copy(os.join(folders, file), os.join(folders, file + '.backup'))
   """