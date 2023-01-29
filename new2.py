import os

root_folder_path = "G:\\My Drive\\Chainsaw Man Chapters"
image_files = []

for root, dirs, files in os.walk(root_folder_path):
    for filename in files:
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image_files.append(filename)

# write the list of image files to a file
with open("image_files_list.txt", "w") as f:
    f.write(str(image_files))