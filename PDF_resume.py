from tkinter import N
from fpdf import FPDF
import json

data_json= open ('resume.json')
resume_raw=json.loads(data_json.read())
pdf = FPDF('P','mm','A4')
pdf.add_page()

pdf.image("bg.png",0 ,0,216,297)

pdf.set_font('Times','B', size=15)
pdf.set_text_color(220,50,50)
pdf.cell(100, 5,txt= "BASIC INFORMATION", ln=1,border=1,align="C",fill=0)
pdf.set_text_color(100,50,50)
pdf.set_font('arial','', size=8)
pdf.cell(100, 5,txt="Name: " + resume_raw["BASIC INFO"]["NAME"], ln=1,border=1,align="C",fill=0)
pdf.cell(100, 5,txt="Age: " + resume_raw["BASIC INFO"]["AGE"], ln=1,border=1,align="C",fill=0)
pdf.cell(100, 5,txt="Birthday: " + resume_raw["BASIC INFO"]["BIRTHDAY"], ln=1,border=1,align="C",fill=0)
pdf.cell(100, 5,txt="Personality: ", ln=5,border=1,align="C",fill=0)
pdf.multi_cell(100,5,txt= resume_raw["BASIC INFO"]["PERSONALITY"], ln=1,border=1,align="C",fill=0)

pdf.set_font('Times','B', size=15)
pdf.set_text_color(220,50,50)
pdf.cell(100, 5,txt= "CONTACT", ln=2,border=1,align="C",fill=0)
pdf.set_text_color(100,50,50)
pdf.set_font('arial','', size=8)
pdf.cell(100,5,txt="Address: " + resume_raw["CONTACT"]["ADDRESS"], ln=1,border=1,align="C",fill=0)
pdf.cell(100,5,txt="Email: " + resume_raw["CONTACT"]["EMAIL"], ln=1,border=1,align="C",fill=0)
pdf.cell(100,5,txt="Phone number: " + resume_raw["CONTACT"]["PHONE NUMBER"], ln=1,border=1,align="C",fill=0)
pdf.cell(100,5,txt="Facebook: " + resume_raw["CONTACT"]["FACEBOOK"], ln=1,border=1,align="C",fill=0)

pdf.set_font('Times','B', size=15)
pdf.set_text_color(220,50,50)
pdf.cell(100,5,txt= "EDUCATION BACKGROUND", ln=2,border=1,align="C",fill=0)

pdf.set_text_color(100,50,50)
pdf.set_font('arial','', size=8)
pdf.cell(100,5,txt= "Primary Education", ln=1,border=1,align="C",fill=0)
pdf.multi_cell(100,5,txt=resume_raw["EDUC BACKGROUND"]["PRIMARY EDUCATION"], ln=1,border=1,align="C",fill=0)

pdf.cell(100,5,txt= "Secondary Education", ln=1,border=1,align="C",fill=0)
pdf.multi_cell(100,5,txt=resume_raw["EDUC BACKGROUND"]["SECONDARY EDUCATION"], ln=1,border=1,align="C",fill=0)

pdf.cell(100,5,txt= "Tertiary Education", ln=1,border=1,align="C",fill=0)
pdf.multi_cell(100,5,txt=resume_raw["EDUC BACKGROUND"]["TERTIARY EDUCATION"], ln=1,border=1,align="C",fill=0)

pdf.set_font('Times','B', size=15)
pdf.set_text_color(220,50,50)
pdf.cell(100,5,txt= "Skills and Goals", ln=2,border=1,align="C",fill=0)
pdf.set_text_color(100,50,50)
pdf.set_font('arial','', size=8)
pdf.cell(100,5,txt= "Skills", ln=1,border=1,align="C",fill=0)
pdf.multi_cell(100, 5,txt=resume_raw["SKILLS AND GOALS"]["PERSONAL SKILLS"],ln=1,border=1,align="C",fill=0)
pdf.cell(100,5,txt= "Goals", ln=1,border=1,align="C",fill=0)
pdf.multi_cell(100,5,txt=resume_raw["SKILLS AND GOALS"]["GOALS"],ln=1,border=1,align="C",fill=0)

pdf.set_font('Times','B', size=15)
pdf.set_text_color(220,50,50)
pdf.cell(100, 5,txt= "Career Background", ln=2,border=1,align="C",fill=0)
pdf.set_text_color(100,50,50)
pdf.set_font('arial','', size=8)
pdf.multi_cell(100, 5,txt=resume_raw["CAREER BACKGROUND"]["JOB1"],ln=1,border=1,align="C",fill=0)
pdf.multi_cell(100, 5,txt=resume_raw["CAREER BACKGROUND"]["JOB2"],ln=1,border=1,align="C",fill=0)

pdf.output("test2.pdf")