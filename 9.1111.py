import os

# prompt user for directory
directory = input("Enter dicrectory to save file: ")
# directory defaults to current directory if user presses enter key
if directory == "":
    directory = "."
# checks that path is valid
assert os.path.exists(directory), "Path does not exist."

# prompt user for filename
filename = input("Enter filename: ")

# prompt for user details
name = input("Enter name: ")
address
