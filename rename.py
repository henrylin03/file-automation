import os
from glob import glob
import shutil

current_folder = os.path.dirname(__file__)
files_folder = os.path.join(current_folder, "files")


def create_test_files(folder=files_folder, file_count=10):
    print(f"Creating {file_count} test files...")

    for i in range(file_count):
        file_name = f"test{i+1}.txt"
        print(f"Creating {file_name}...")

        with open(os.path.join(folder, file_name), "w+") as fp:
            fp.write(f"This is a test file. This is test file {i+1} of {file_count}.")
            fp.close()

        print("Done!")


def add_prefix(folder=files_folder):
    print("Please enter the prefix to be added to the files: ")
    prefix = input()
    print("Please enter the pattern of files that will have this prefix (eg *.txt): ")
    pattern = input()

    os.chdir(folder)

    print(f"Adding prefix '{prefix}' to all files...")
    [os.rename(f, f"{prefix}{f}") for f in glob(pattern)]
    print("Done!")


def delete_old_files(folder=files_folder):
    print(
        "We have now renamed your files. Would you like to delete your previous files? (Y/N)"
    )
    delete_response = input()

    if delete_response.lower() == "yes" or delete_response.lower() == "y":
        print("deleting...")
    else:
        print("no worries!")


def main():
    ### comment out the `create_test_files()` function if you do not need to create test files ###
    # create_test_files()
    # print(f"Please place all files in: {folder}.")
    add_prefix()
    delete_old_files()
    # print(os.path.dirname(__file__))


main()
