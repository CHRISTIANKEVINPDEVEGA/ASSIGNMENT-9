from fpdf import FPDF
import json

data_json= open ('resume.json')
resume_raw=json.loads(data_json.read())
print(resume_raw)