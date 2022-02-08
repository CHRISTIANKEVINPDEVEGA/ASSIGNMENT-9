from fpdf import FPDF
import json

with open("D:\PLD tasks\PLD assignments\9th assignment\Assignment9\ASSIGNMENT-9/resume.json") as json_file:
 data = json.load(json_file)




pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(txt = data["BASIC INFORMATION"]["NAME"], ln=1)
pdf.cell(txt = data["BASIC INFORMATION"]["AGE"], ln=2)