import os

path = input()


if not os.path.exists(path):
    print("Path Does Not Exist")

if not os.access(path, os.R_OK):
    print("Not Readable")
else:
    print("Readable")

if not os.access(path, os.W_OK):
    print("Not Writable")
else:
    print("Writable")

if not os.access(path, os.X_OK):
    print("Not Executable")
else:
    print("Executable")