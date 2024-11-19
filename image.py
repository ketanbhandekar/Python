""" PDF TO IMAGE"""

from pdf2image import convert_from_path

old_pdf=convert_from_path("PDFs/sample-invoice.pdf",poppler_path=r"C:\Users\Admin\Desktop\Python_api\poppler-24.02.0\Library\bin")

for i in range(len(old_pdf)):
    old_pdf[i].save("new" + str(i)+ ".jpg","JPEG")
