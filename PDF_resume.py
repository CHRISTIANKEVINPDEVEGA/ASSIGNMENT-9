from tkinter import N
from fpdf import FPDF
import json

data_json= open ('resume.json')
resume_raw=json.loads(data_json.read())
pdf = FPDF('P','mm','Letter')
pdf.add_page()

pdf.set_font('Times','B', size=30)
pdf.set_text_color(220,50,50)
pdf.cell(txt= "BASIC INFORMATION", ln=1)
pdf.set_text_color(100,50,50)
pdf.set_font('arial','', size=8)
pdf.cell(txt="Name: " + resume_raw["BASIC INFO"]["NAME"], ln=1)
pdf.cell(txt="Age: " + resume_raw["BASIC INFO"]["AGE"], ln=1)
pdf.cell(txt="Birthday: " + resume_raw["BASIC INFO"]["BIRTHDAY"], ln=1)
pdf.cell(txt="Personality: ", ln=5)
pdf.multi_cell(120,5,txt= resume_raw["BASIC INFO"]["PERSONALITY"]["P1"] + resume_raw["BASIC INFO"]["PERSONALITY"]["P2"], ln=1,)

pdf.set_font('Times','B', size=30)
pdf.set_text_color(220,50,50)
pdf.cell(txt= "CONTACT", ln=2)
pdf.set_text_color(100,50,50)
pdf.set_font('arial','', size=8)
pdf.cell(txt="Address: " + resume_raw["CONTACT"]["ADDRESS"], ln=1)
pdf.cell(txt="Email: " + resume_raw["CONTACT"]["EMAIL"], ln=1)
pdf.cell(txt="Phone number: " + resume_raw["CONTACT"]["PHONE NUMBER"], ln=1)
pdf.cell(txt="Facebook: " + resume_raw["CONTACT"]["FACEBOOK"], ln=1)

pdf.set_font('Times','B', size=30)
pdf.set_text_color(220,50,50)
pdf.cell(txt= "EDUCATION BACKGROUND", ln=2)

pdf.set_text_color(100,50,50)
pdf.set_font('arial','', size=8)
pdf.cell(txt= "Primary Education", ln=1)
pdf.cell(txt="School: " + resume_raw["EDUC BACKGROUND"]["PRIMARY EDUCATION"]["NAME OF SCHOOL"], ln=1)
pdf.cell(txt="School Info: " + resume_raw["EDUC BACKGROUND"]["PRIMARY EDUCATION"]["SCHOOL INFO"], ln=1)

pdf.cell(txt= "Secondary Education", ln=1)
pdf.cell(txt="School: " + resume_raw["EDUC BACKGROUND"]["SECONDARY EDUCATION"]["NAME OF SCHOOL"], ln=1)
pdf.cell(txt="School Info: " + resume_raw["EDUC BACKGROUND"]["SECONDARY EDUCATION"]["SCHOOL INFO"], ln=1)

pdf.cell(txt= "Tertiary Education", ln=1)
pdf.cell(txt="School: " + resume_raw["EDUC BACKGROUND"]["TERTIARY EDUCATION"]["NAME OF SCHOOL"], ln=1)
pdf.cell(txt="School Info: " + resume_raw["EDUC BACKGROUND"]["TERTIARY EDUCATION"]["SCHOOL INFO"], ln=1)
pdf.cell(txt="College Degree: " + resume_raw["EDUC BACKGROUND"]["TERTIARY EDUCATION"]["COLLEGE DEGREE"], ln=1)

pdf.set_font('Times','B', size=30)
pdf.set_text_color(220,50,50)
pdf.cell(txt= "Skills and Goals", ln=2)
pdf.set_text_color(100,50,50)
pdf.set_font('arial','', size=8)
pdf.cell(txt= "Primary Education", ln=1)
pdf.cell(txt="School: " + resume_raw["SKILLS AND GOALS"]["PERSONAL SKILLS"]["SKILL_1"], ln=1)






pdf.output("test2.pdf")