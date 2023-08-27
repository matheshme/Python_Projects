# First we have to install the modeule for install the module use the below command
# pip install pdf2docx
from pdf2docx import Converter
# convert pdf to docx
cv = Converter("sample.pdf")
cv.convert("sample.docx", start=0, end=None)
cv.close()