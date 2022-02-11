from email.mime import image
from multiprocessing import managers
from tkinter import N
from fpdf import FPDF
import json


data_json= open ('resume.json')
resume_raw=json.loads(data_json.read())

NAME= resume_raw["BASIC INFO"]["NAME"]
AGE=resume_raw["BASIC INFO"]["AGE"]
BIRTHDAY=resume_raw["BASIC INFO"]["BIRTHDAY"]
PERSONALITY=resume_raw["BASIC INFO"]["PERSONALITY"]
ADDRESS=resume_raw["CONTACT"]["ADDRESS"]
EMAIL=resume_raw["CONTACT"]["EMAIL"]
PHONE_NUM=resume_raw["CONTACT"]["PHONE NUMBER"]
FB=resume_raw["CONTACT"]["FACEBOOK"]

PRIM_EDUC=resume_raw["EDUC BACKGROUND"]["PRIMARY EDUCATION"]
SEC_EDUC=resume_raw["EDUC BACKGROUND"]["SECONDARY EDUCATION"]
TER_EDUC=resume_raw["EDUC BACKGROUND"]["TERTIARY EDUCATION"]
AWARDS_ACCOMP=1
PERSONAL_SKILLS=resume_raw["SKILLS AND GOALS"]["PERSONAL SKILLS"]
GOALS=resume_raw["SKILLS AND GOALS"]["GOALS"]
JOB1=resume_raw["CAREER BACKGROUND"]["JOB1"]
JOB2=resume_raw["CAREER BACKGROUND"]["JOB2"]



pdf = FPDF('P','mm','A4')
pdf.set_top_margin(20)
pdf.set_left_margin(19)
pdf.set_right_margin(15)
pdf.add_page()


pdf.image("bg.png",0 ,0,216,297)
pdf.set_font('Times','B', size=15)
pdf.set_text_color(255,25,60)
pdf.set_fill_color(223,220,213)
pdf.cell(90, 187,txt= "Image", ln=0,border=1,align="B",fill=1)

pdf.image("boi.jpg",19 ,20,80,80)
pdf.set_font('Times','B', size=15)
pdf.set_text_color(220,50,50)

pdf.set_font('Times','B', size=15)
pdf.set_text_color(220,50,50)
pdf.cell(90, 5,txt= "BASIC INFORMATION", ln=2,border=1,align="L",fill=0)
pdf.set_text_color(100,50,50)
pdf.set_font('arial','', size=8)
pdf.cell(90, 7,txt="Name: " + NAME, ln=2,border=1,align="L",fill=0)
pdf.cell(90, 7,txt="Age: " + AGE, ln=2,border=1,align="L",fill=0)
pdf.cell(90, 7,txt="Birthday: " + BIRTHDAY, ln=2,border=1,align="L",fill=0)
pdf.multi_cell(90, 7,txt="Personality:\n" + PERSONALITY, ln=2,border=1,align="L",fill=0)


pdf.set_font('Times','B', size=15)
pdf.set_text_color(220,50,50)
pdf.cell(90,7,txt= "EDUCATION BACKGROUND", ln=2,border=1,align="L",fill=0)
pdf.set_text_color(100,50,50)
pdf.set_font('arial','', size=8)
pdf.multi_cell(90,7,txt= "Primary Education:\n" + PRIM_EDUC, ln=2,border=1,align="L",fill=0)
pdf.multi_cell(90,7,txt= "Secondary Education:\n"+ SEC_EDUC, ln=2,border=1,align="L",fill=0)


pdf.multi_cell(90,7,txt= "Tertiary Education\n" + TER_EDUC, ln=2,border=1,align="L",fill=0)




pdf.set_font('Times','B', size=15)
pdf.set_text_color(220,50,50)
pdf.cell(90,7,txt= "Skills and Goals", ln=2,border=1,align="L",fill=0)
pdf.set_text_color(100,50,50)
pdf.set_font('arial','', size=8)
pdf.cell(90,7,txt= "Skills", ln=2,border=1,align="L",fill=0)
pdf.multi_cell(90, 7,txt=resume_raw["SKILLS AND GOALS"]["PERSONAL SKILLS"],ln=2,border=1,align="L",fill=0)
pdf.cell(90,7,txt= "Goals", ln=2,border=1,align="L",fill=0)
pdf.multi_cell(90,7,txt=resume_raw["SKILLS AND GOALS"]["GOALS"],ln=1,border=1,align="L",fill=0)

pdf.set_font('Times','B', size=15)
pdf.set_text_color(220,50,50)
pdf.cell(180, 7,txt= "Career Background", ln=1,border=1,align="L",fill=0)
pdf.set_text_color(100,50,50)
pdf.set_font('arial','', size=8)
pdf.multi_cell(180, 7,txt=JOB1,ln=1,border=1,align="L",fill=0)
pdf.multi_cell(180, 7,txt=JOB2,ln=1,border=1,align="L",fill=0)



pdf.set_font('Times','B', size=15)
pdf.set_text_color(220,50,50)
pdf.cell(180, 7,txt= "CONTACT", ln=1,border=1,align="L",fill=0)
pdf.set_text_color(100,50,50)
pdf.set_font('arial','', size=8)
pdf.cell(180,7,txt="Address: " + ADDRESS, ln=1,border=1,align="L",fill=0)
pdf.cell(180,7,txt="Email: " + EMAIL, ln=1,border=1,align="L",fill=0)
pdf.cell(180,7,txt="Phone number: " + PHONE_NUM, ln=1,border=1,align="L",fill=0)
pdf.cell(180,7,txt="Facebook: " + FB, ln=0,border=1,align="L",fill=0)



FB
pdf.output("test2.pdf")