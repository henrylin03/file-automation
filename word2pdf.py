from win32com import client
import docx
import os
from pathlib import Path
from glob import glob

cwd = os.path.dirname(__file__)
test_folder = os.path.join(cwd, "test_files")


def create_test_docx(doc_count=10):
    print("\nEntering testing mode...")
    doc_count = input(
        "\nPlease enter the number of test Word docs you would like to create: \n"
    )

    Path(test_folder).mkdir(parents=True, exist_ok=True)

    print(f"\nCreating {doc_count} test Word docs...")

    for i in range(int(doc_count)):
        doc_name = f"test{i+1}.docx"

        print(f"\nCreating {doc_name}...")
        doc = docx.Document()
        doc.add_paragraph(f"This is test doc #{i+1} of {doc_count}")

        doc.save(os.path.join(test_folder, doc_name))
        print("\n\tDone!")


def convert(folder_name=cwd):
    word_docs_list = glob(os.path.join(folder_name, "*.doc*"))
    print(f"\nConverting {len(word_docs_list)} Word docs in {folder_name}...")

    for w in word_docs_list:
        doc_name = w.rsplit("\\")[-1]
        pdf_path = w.replace(".docx", ".pdf").replace(".doc", ".pdf")

        print(f"\n\tConverting '{doc_name}' to PDF...")

        word = client.DispatchEx("Word.Application")
        doc = word.Documents.Open(w)
        doc.SaveAs(pdf_path, FileFormat=17)
        doc.Close()
        word.Quit()

        print("\tDone!")

    print(
        f"\n{len(word_docs_list)} out of {len(word_docs_list)} Word docs converted to PDF!"
    )


def main():
    print(
        """
    
    *** Welcome to Word2PDF! *** 
    Quickly convert all your Word docs to PDFs!
    
    """
    )

    start_input = input("Press enter to begin!\n")

    if start_input.lower() == "test":
        create_test_docx()
        convert(test_folder)
    else:
        convert()


if __name__ == "__main__":
    main()
