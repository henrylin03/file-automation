import os
import time
from glob import glob
from pathlib import Path
import shutil

cwd = os.path.dirname(__file__)
backup_parent_folder = os.path.join(cwd, "prev_files")
test_files_folder = os.path.join(cwd, "test_files")


def prefix_triage(files_folder=cwd):
    while True:
        prefix_choice = input(
            """
Are you looking to:
(a) add a prefix to files
(b) remove a prefix from files
(c) quit Rename\n
"""
        )
        add_choices = ["(a)", "a", "add"]
        remove_choices = ["(b)", "b", "remove"]
        quit_choices = ["(c)", "c", "quit"]

        if prefix_choice.lower() in add_choices:
            add_prefix(files_folder)
        elif prefix_choice.lower() in remove_choices:
            del_prefix(files_folder)
        elif prefix_choice.lower() in quit_choices:
            break
        else:
            print("\nSorry, I did not understand.")


def add_prefix(files_folder=cwd):
    while True:
        prefix = input("\nPlease enter the prefix to be added to the files: ")

        if prefix:
            pattern_input = input(
                "\n(Optional) Please enter the pattern of files that will have this prefix (eg *.docx): "
            )
            backup_folder = backup_files(files_folder)
            pattern = pattern_input if pattern_input else "*.*"
            os.chdir(files_folder)
            applied_files = [f for f in glob(pattern) if os.path.isfile(f)]
            print(f"\nAdding prefix '{prefix}' to {len(applied_files)} files...")
            [os.rename(f, f"{prefix}{f}") for f in applied_files]
            print("\n\tDone!")
            delete_backup_files(backup_folder)
            break


def del_prefix(files_folder=cwd):
    while True:
        prefix = input("\nPlease enter the prefix to be removed from the files: ")

        if prefix:
            pattern_input = input(
                "\n(Optional) Please enter the pattern of files that will have this prefix removed (eg *.docx): "
            )
            backup_folder = backup_files(files_folder)
            pattern = pattern_input if pattern_input else "*.*"
            os.chdir(files_folder)
            applied_files = [f for f in glob(pattern) if os.path.isfile(f)]
            print(f"\Removing prefix '{prefix}' from {len(applied_files)} files...")
            [os.rename(f, f.removeprefix(prefix)) for f in applied_files]
            print("\n\tDone!")
            delete_backup_files(backup_folder)
            break


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
    backup_files_list = next(os.walk(backup_folder), (None, None, []))[2]

    while True:
        delete_response = input(
            "\nWe have now renamed your files. Would you like to delete your previous files? (Y/N)\n"
        )
        if delete_response.lower() == "yes" or delete_response.lower() == "y":
            print(f"\nDeleting previous files from /{backup_folder_name}...")
            shutil.rmtree(backup_folder)
            print(f"\n\t{len(backup_files_list)} files deleted!")
            break
        elif delete_response.lower() == "no" or delete_response.lower() == "n":
            print(f"\nPrevious files are kept in /{backup_folder_name}.")
            break
        else:
            print("\nSorry, I did not understand. Please try again.\n")


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
    start_input = input("\nWelcome to Rename!\nPress enter to begin")
    if start_input == "test":
        create_test_files()
        prefix_triage(test_files_folder)
    else:
        prefix_triage()


if __name__ == "__main__":
    main()
