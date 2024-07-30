import os
# specify the directory you wan to use
directory_path = '/java'
# list all the files and directories in the specified path
contents = os.listdir(directory_path)
# print each files and directory name
for item in contents:
    print(item)