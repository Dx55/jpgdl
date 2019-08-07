#By Dx55

from PyPDF2 import PdfFileWriter, PdfFileReader

output_pdf = PdfFileWriter()

with open('C:/Users/Akira/Desktop/Jojo.pdf', 'rb') as readfile:
    input_pdf = PdfFileReader(readfile)
for page in reversed(input_pdf.pages):
    output_pdf.addPage(page)
with open('C:/Users/Akira/Desktop/output.pdf', "wb") as writefile:
    output_pdf.write(writefile)