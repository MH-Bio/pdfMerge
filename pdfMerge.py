from pypdf import PdfMerger
from os import listdir, path

pdfs = listdir()

merger = PdfMerger()

for pdf in pdfs:
    if pdf == path.basename(__file__):
        continue
    merger.append(pdf)

merger.write("result.pdf")
merger.close()