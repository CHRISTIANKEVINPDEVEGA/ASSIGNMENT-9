from fpdf import FPDF
import json

data_json= open ('resume.json')
resume_raw=json.loads(data_json.read())
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=16)
pdf.cell(txt=resume_raw["BASIC INFORMATION"]["NAME"], ln=1)
pdf.output("test.pdf")