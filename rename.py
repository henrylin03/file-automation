import os
import time
from glob import glob
from pathlib import Path
import shutil

main_folder = os.path.dirname(__file__)
backup_parent_folder = os.path.join(main_folder, "prev_files")
test_files_folder = os.path.join(main_folder, "test_files")


def backup_files(files_folder=main_folder):
    datetime_suffix = time.strftime("%Y%m%d-%H%M")
    backup_folder_name = "/prev_files" + "f/{datetime_suffix}"
    backup_folder = os.path.join(backup_parent_folder, datetime_suffix)
    files_list = next(os.walk(files_folder), (None, None, []))[2]

    print(f"Backing up all files to {backup_folder_name}...")

    Path(backup_folder).mkdir(parents=True, exist_ok=True)
    for f in files_list:
        source = os.path.join(files_folder, f)
        shutil.copy2(source, backup_folder)
    print(f"\t{len(files_list)} files backed up!")

    backed_up_files = [os.path.join(backup_folder, f) for f in files_list]
    return backed_up_files


def delete_backup_files():
    while True:
        delete_response = input(
            "We have now renamed your files. Would you like to delete your previous files? (Y/N)\n"
        )
        if delete_response.lower() == "yes" or delete_response.lower() == "y":
            print("Deleting previous files...")
            backup_files = glob(os.path.join(backup_parent_folder, "*.*"))
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


def add_prefix(files_folder=main_folder):
    print("Please enter the prefix to be added to the files: ")
    prefix = input()
    print("Please enter the pattern of files that will have this prefix (eg *.txt): ")
    pattern = input()  ## what if I just want to apply to all files!

    os.chdir(files_folder)

    backup_files(files_folder)

    print(f"Adding prefix '{prefix}' to all files...")

    [os.rename(f, f"{prefix}{f}") for f in glob(pattern)]

    print("\tDone!")


def create_test_files(folder=test_files_folder, file_count=10):
    test_input = input(
        "Press any key to create test files. Type 'skip' if you would like to skip.\n"
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
    create_test_files()
    add_prefix(test_files_folder)
    delete_backup_files()


if __name__ == "__main__":
    main()
