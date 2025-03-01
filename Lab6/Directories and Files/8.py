import os

path = "."

file_name = input()

if os.path.exists(f"{path}/{file_name}.txt"):
    os.remove(f"{path}/{file_name}.txt")
else:
    print(f"{file_name} does not exist")