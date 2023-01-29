import os
import random
import cv2

root_folder_path = "C:\\Users\\franc\\Desktop\\Chainsaw Man Chapters"

for root, dirs, files in os.walk(root_folder_path):
    for filename in files:
        if filename.endswith(".png") or filename.endswith(".jpg"):
            # read the image
            img = cv2.imread(os.path.join(root, filename))
            print(filename)

            # resize the image while keeping aspect ratio
            height, width = img.shape[:2]
            new_height = height - 200
            new_width = int(width * new_height / height)
            img = cv2.resize(img, (new_width, new_height), interpolation = cv2.INTER_LANCZOS4)

            random_letter = chr(random.randint(97, 122))

            # create a new file name
            new_filename = filename[:-4] + random_letter + ".png"

            # save the image
            cv2.imwrite(os.path.join(root, new_filename), img)
            # remove the original file
            os.remove(os.path.join(root, filename))
