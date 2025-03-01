import os
import os.path
path = input("Enter a path to check: ")

if os.path.exists(path):
    print(f"Path '{path}' exists")

    dirname = os.path.dirname(path)
    basename = os.path.basename(path)

    print(f"Directory portion: {dirname}")
    print(f"Filename portion: {basename}")
else:
    print(f"Path '{path}' does not exist")



