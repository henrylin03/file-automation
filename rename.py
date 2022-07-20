import os
from glob import glob
from pathlib import Path
import shutil

current_folder = os.path.dirname(__file__)
backup_folder = os.path.join(current_folder, "prev_files")
test_files_folder = os.path.join(current_folder, "files")


def backup_files(files_list, folder=current_folder):
    print("Backing up current files to the /prev_files folder...")

    Path(backup_folder).mkdir(parents=True, exist_ok=True)

    destination = backup_folder
    for f in files_list:
        source = os.path.join(folder, f)
        shutil.copy2(source, destination)
    print("Done!")


def delete_backup_files():
    while True:
        delete_response = input(
            "We have now renamed your files. Would you like to delete your previous files? (Y/N)"
        )
        if delete_response.lower() == "yes" or delete_response.lower() == "y":
            print("Deleting previous files...")
            backup_files = glob(os.path.join(backup_folder, "*.*"))
            for f in backup_files:
                f_name = f.rsplit("\\", 1)[-1]
                print(f"\tDeleting {f_name}...")
                os.remove(f)
                print("Done!")
            break
        elif delete_response.lower() == "no" or delete_response.lower() == "n":
            print("Previous files are kept in the /prev_files folder.")
            break
        else:
            print("Sorry, I did not understand. Please try again.\n")


def add_prefix():
    print("Please enter the prefix to be added to the files: ")
    prefix = input()
    print("Please enter the pattern of files that will have this prefix (eg *.txt): ")
    pattern = input()

    os.chdir(current_folder)

    backup_files(glob(pattern), current_folder)

    print(f"Adding prefix '{prefix}' to all files...")
    [os.rename(f, f"{prefix}{f}") for f in glob(pattern)]
    print("Done!")
    ## need to add debugging for "File already exists error" when the final, renamed file already exists!


def create_test_files(folder=test_files_folder, file_count=10):
    test_input = input(
        "Press any key to create test files. Type 'skip' if you would like to skip."
    )

    if test_input.lower() == "skip":
        pass
    else:
        Path(folder).mkdir(parents=True, exist_ok=True)

        print(f"Creating {file_count} test files...")

        for i in range(file_count):
            file_name = f"test{i+1}.txt"
            print(f"Creating {file_name}...")

            with open(os.path.join(folder, file_name), "w+") as fp:
                fp.write(
                    f"This is a test file. This is test file {i+1} of {file_count}."
                )
                fp.close()

            print("Done!")


def main():
    input("Press any key to begin!\n")
    create_test_files()  ## need to consider how to ensure that code is used for prod differently than if it were to be used for testing -- we don't really even need this function in main() then!
    # print(f"Please place all files in: {folder}.")
    add_prefix(test_files_folder)
    delete_backup_files()


if __name__ == "__main__":
    main()
