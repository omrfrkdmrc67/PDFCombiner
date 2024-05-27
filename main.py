from pypdf import PdfWriter

pdfs = ['sample.pdf','sample2.pdf']

merger = PdfWriter()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()