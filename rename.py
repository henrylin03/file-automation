import os

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


def replace_prefix(folder=files_folder):
    pass


def main():
    ### comment out the `create_test_files()` function if you do not need to create test files ###
    # create_test_files()
    pass
    # print(os.path.dirname(__file__))


main()
