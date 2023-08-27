# First we have to install the modeule for install the module use the below command
# pip install docx2pdf
from docx2pdf import convert
# convert("input.docx")
convert("sample.docx", "output.pdf")