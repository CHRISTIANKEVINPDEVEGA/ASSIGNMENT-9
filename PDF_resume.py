from email.mime import image
from multiprocessing import managers
from re import T
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
AWARDS_ACCOMP=resume_raw["EDUC BACKGROUND"]["AWARDS AND ACCOMPLISHMENTS"]
PERSONAL_SKILLS=resume_raw["SKILLS AND GOALS"]["PERSONAL SKILLS"]
GOALS=resume_raw["SKILLS AND GOALS"]["GOALS"]
JOB1=resume_raw["CAREER BACKGROUND"]["JOB1"]
JOB2=resume_raw["CAREER BACKGROUND"]["JOB2"]



pdf = FPDF('P','mm','A4')
pdf.set_top_margin(25)
pdf.set_left_margin(15)
pdf.set_right_margin(15)
pdf.add_page()

#For the background,the picture and txt color
pdf.image("bg.png",0 ,0,210,297)
pdf.set_fill_color(73,117,156)
pdf.set_text_color(1,1,1)
pdf.set_font('Times','B', size=15)
pdf.cell(90, 112,ln=0,border=0,fill=1)
pdf.image("boi.jpg",20 ,40,80,80)


#BASIC INFORMATION
pdf.cell(90, 6,txt= "BASIC INFORMATION", ln=2,border="B",align="L",fill=0)
pdf.set_font('arial','B', size=8)
pdf.cell(90, 6,txt="Name: " + NAME, ln=2,border=0,align="L",fill=0)
pdf.cell(90, 6,txt="Age: " + AGE, ln=2,border=0,align="L",fill=0)
pdf.cell(90, 6,txt="Birthday: " + BIRTHDAY, ln=2,border=0,align="L",fill=0)
pdf.multi_cell(90, 6,txt="Personality:\n" + PERSONALITY, ln=2,border=0,align="L",fill=0)

#EDUCATION BACKGROUND
pdf.set_font('Times','B', size=15)
pdf.cell(90,6,txt= "EDUCATION BACKGROUND", ln=2,border="B",align="L",fill=0)
pdf.set_font('arial','B', size=8)
pdf.cell(90,6,txt= "Primary Education", ln=2,border="B",align="L",fill=0)
pdf.multi_cell(90,6,txt=PRIM_EDUC, ln=2,border=0,align="L",fill=0)
pdf.cell(90,6,txt= "Secondary Education", ln=2,border="B",align="L",fill=0)
pdf.multi_cell(90,6,txt=SEC_EDUC, ln=2,border=0,align="L",fill=0)
pdf.cell(90,6,txt= "Tertiary Education", ln=2,border="B",align="L",fill=0)
pdf.multi_cell(90,6,txt= TER_EDUC, ln=1,border=0,align="L",fill=0)

#Awards and Accomplishments
pdf.cell(180,6,txt= "Awards and Accomplishments", ln=2,border="B",align="L",fill=0)
pdf.multi_cell(180,6,txt= AWARDS_ACCOMP, ln=1,border=0,align="L",fill=0)

#Skills and Goals
pdf.set_font('Times','B', size=15)
pdf.cell(180,6,txt= "Skills and Goals", ln=2,border="B",align="L",fill=0)
pdf.set_font('arial','B', size=8)
pdf.cell(180,5,txt= "Skills", ln=2,border="B",align="L",fill=0)
pdf.multi_cell(180, 6,txt= PERSONAL_SKILLS ,ln=2,border=0,align="L",fill=0)
pdf.cell(180,6,txt= "Goals", ln=2,border="B",align="L",fill=0)
pdf.multi_cell(180,6,txt= GOALS,ln=1,border=0,align="L",fill=0)

#Career Background
pdf.set_font('Times','B', size=15)
pdf.cell(180, 6,txt= "Career Background", ln=1,border=0,align="L",fill=0)
pdf.set_font('arial','B', size=8)
pdf.multi_cell(180, 6,txt=JOB1,ln=1,border="T",align="L",fill=0)
pdf.multi_cell(180, 6,txt=JOB2,ln=1,border="T",align="L",fill=0)

#CONTACT
pdf.set_font('Times','B', size=15)
pdf.cell(180, 6,txt= "CONTACT", ln=1,border="B",align="L",fill=0)
pdf.set_font('arial','', size=8)
pdf.cell(180,5,txt="Address: " + ADDRESS, ln=1,border=0,align="L",fill=0)
pdf.cell(180,6,txt="Email: " + EMAIL, ln=1,border=0,align="L",fill=0)
pdf.cell(180,5,txt="Phone number: " + PHONE_NUM, ln=1,border=0,align="L",fill=0)
pdf.cell(180,6,txt="Facebook: " + FB, ln=0,border=0,align="L",fill=0)



pdf.output("test2.pdf")