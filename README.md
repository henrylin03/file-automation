# Rename
Python app to quickly rename files in a folder.

Currently, **Rename** supports renaming specified files in a folder, including:
- Adding a prefix

## How to Use
1. Download `rename.py` and place in folder with the files you want to rename.
2. Run `rename.py` and follow the prompts.

### Backup Files
A copy of all files are copied to the `/prev_files` folder before renaming, allowing you to restore previous files, if required.

### Specifying Files Using Regex
Instead of Renaming all files in a folder, you may wish to only apply the change to a select set of files.

For example, 
- If you are only Renaming Word documents:

        *.docx

- If you are only Renaming Excel spreadsheets that start with 'Draft':
        
        Draft*.xlsx

Other than the wildcard (`*`), Rename supports all regular expressions (regex). Please see the [regex cheatsheet](https://cheatography.com/davechild/cheat-sheets/regular-expressions/) for more information.

### Testing
If you don't have any specific files to rename yet and just want to test the code, you can use the `create_test_files()` function to generate test .txt files in a `/test_files` folder for you to manipulate.

## Issues/Questions/Enhancements?
If you have any questions, experienced any issues, and/or have any suggestions for enhancements, please raise a GitHub Issue and tag it. Thank you for your support!
