import ast
import random
from auth import *

def getRandomFile():
    drive = getGoogleAuth()

    file_list = []

    file_list = drive.ListFile().GetList()
    print_list = []
    for file in file_list:
        print_list.append(file['title'])
    return print_list

if __name__ == "__main__":
    print_list = getRandomFile()
    print(print_list)