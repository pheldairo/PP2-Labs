import os


def list_directories_files(path):
    directories = []
    files = []
    all_directories_files = []

    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            directories.append(entry)
            all_directories_files.append(entry)
        else:
            files.append(entry)
            all_directories_files.append(entry)

    print("Directories:", *directories)
    print("Files:", *files)
    print("All Directories and Files:", *all_directories_files)


path = '/home/leph/Coding/'
list_directories_files(path)