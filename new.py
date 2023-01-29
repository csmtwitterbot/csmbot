import os
import random
import cv2
import numpy as np
from PIL import Image


root_folder_path = "I:\\My Drive\\Oshi no Ko"

for root, dirs, files in os.walk(root_folder_path):
    for filename in files:
        if filename.endswith(".png") or filename.endswith(".jpg"):
            # read the image
            img = cv2.imread(os.path.join(root, filename))
            print(filename)

            random_letter = chr(random.randint(97, 122))

            # create a new file name
            new_filename = filename[:-4] + random_letter + ".png"

            # Get the size of the image file in bytes
            file_size = os.path.getsize(os.path.join(root, filename))

            # Convert the file size to megabytes
            file_size_mb = file_size / 1024 / 1024

            # Check if the file size is greater than 4.8 MB
            if file_size_mb > 4.8:
                # Load the image
                img = Image.open(os.path.join(root, filename))

                # Get the size of the original image
                width, height = img.size

                # Calculate the size of the resized image
                resized_width = width // 3
                resized_height = height // 3

                # Resize the image
                img_resized = img.resize((resized_width, resized_height), Image.ANTIALIAS)

                # Save the resized image
                img_resized.save(os.path.join(root, filename))
            else:
                # The file size is not greater than 4.8 MB, so no resizing is necessary
                pass
