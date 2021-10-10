import win32com.client
import docx
import os
import sys

# function to create test Word docs:
def create_docx(doc_count):
    for i in range(doc_count):
        doc = docx.Document()

        doc.add_paragraph(f"This is test doc #{i+1}")

        doc_title = f"test_doc{i+1}"
        doc.save(f"{doc_title}.docx")


# change the number inside the brackets below to change the number of test Word docs generated
create_docx(3)

# converting Word docs to corresponding PDFs
wdFormatPDF = 17  # this is Word's numeric code for PDFs


def word2pdf_converter(file):
    in_file = os.path.abspath(file)
    out_file = os.path.abspath(file.replace(".docx", ".pdf").replace(".doc", ".pdf"))
    word = win32com.client.Dispatch("Word.Application")
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()


if len(sys.argv) > 1:  # this means that the user introduced file paths
    for file in sys.argv:
        if file.endswith(".docx") or file.endswith(".docx"):
            word2pdf_converter(file)
else:  # this means the user did not introduce file paths, so the current path is selected
    for file in os.listdir("."):
        if file.endswith(".docx") or file.endswith(".docx"):
            word2pdf_converter(file)
