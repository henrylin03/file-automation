import os
import time
from glob import glob
from pathlib import Path
import shutil

cwd = os.path.dirname(__file__)
backup_parent_folder = os.path.join(cwd, "prev_files")
test_files_folder = os.path.join(cwd, "test_files")


def backup_files(files_folder=cwd):
    datetime_suffix = time.strftime("%Y%m%d-%H%M%S")
    backup_folder = os.path.join(backup_parent_folder, datetime_suffix)
    backup_folder_name = backup_folder.rsplit("\\", 1)[-1]
    files_list = next(os.walk(files_folder), (None, None, []))[2]

    print(f"\nBacking up all files to '{backup_folder_name}'...")

    Path(backup_folder).mkdir(parents=True, exist_ok=True)
    for f in files_list:
        source = os.path.join(files_folder, f)
        shutil.copy2(source, backup_folder)
    print(f"\n\t{len(files_list)} files backed up!")

    return backup_folder


def delete_backup_files(backup_folder):
    backup_folder_name = backup_folder.rsplit("\\", 1)[-1]
    backup_files_count = len(
        [f for f in os.listdir(backup_folder) if os.path.isfile(f)]
    )

    while True:
        delete_response = input(
            "We have now renamed your files. Would you like to delete your previous files? (Y/N)\n"
        )
        if delete_response.lower() == "yes" or delete_response.lower() == "y":
            print("\nDeleting previous files...")
            shutil.rmtree(backup_folder)
            print(f"\tDeleted {backup_files_count} files in {backup_folder_name}")
            break
        elif delete_response.lower() == "no" or delete_response.lower() == "n":
            print("\nPrevious files are kept in the backup folder.")
            break
        else:
            print("\nSorry, I did not understand. Please try again.\n")


def add_prefix(files_folder=cwd):
    print("Please enter the prefix to be added to the files: ")
    prefix = input()
    print("\nPlease enter the pattern of files that will have this prefix (eg *.txt): ")
    pattern = input()  ## what if I just want to apply to all files!

    os.chdir(files_folder)
    backup_folder = backup_files(files_folder)

    print(f"\nAdding prefix '{prefix}' to files...")
    [os.rename(f, f"{prefix}{f}") for f in glob(pattern)]
    print("\tDone!")

    delete_backup_files(backup_folder)


def del_prefix(files_folder=cwd):
    prefix = input("Please enter the prefix to be removed from the files: ")

    os.chdir(files_folder)
    backup_folder = backup_files(files_folder)

    print(f"\nRemoving prefix '{prefix}' from files...")
    files_list = next(os.walk(files_folder), (None, None, []))[2]
    [os.rename(f, f.removeprefix(prefix)) for f in files_list]
    print("\tDone!")

    delete_backup_files(backup_folder)


def create_test_files(folder=test_files_folder, file_count=10):
    test_input = input(
        "\nPress enter to create test files. Type 'skip' if you would like to skip.\n"
    )

    if test_input.lower() == "skip":
        pass
    else:
        Path(folder).mkdir(parents=True, exist_ok=True)

        print(f"\nCreating {file_count} test files...")

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
    input("Press enter to begin!")
    create_test_files()
    # add_prefix(test_files_folder)
    del_prefix(test_files_folder)


if __name__ == "__main__":
    main()
