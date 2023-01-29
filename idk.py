import os

root_dir = "C:\\Users\\franc\\Desktop\\Chainsaw Man Chapters"
filenames_list = []

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        filenames_list.append(filename)

with open('file_list.txt', 'w') as file:
    # Write a string to the file
    file.write(str(filenames_list))