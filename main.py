import os
from fpdf import FPDF
import webbrowser

# Collect user details
name = input("Enter your full name: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
summary = input("Write a short professional summary: ")
education = input("Enter your educatio details: ")
linkedin = input("Enter your LinkedIn profile URL: ")
skills = input("Enter your skills (seperate with commas): ")
lang = input("Enter the languages you are familiar with(seperate with commas): ")
experience = input("Enter your Work Experience: ")


# Create PDF object
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", style='B', size=20)

# Add Name
pdf.cell(200, 10, name, ln=True, align='C')
pdf.ln(10)

# Add Contact Info
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, f"Email: {email}", ln=True, align='L')
pdf.cell(200, 10, f"Phone: {phone}", ln=True, align='L')
pdf.ln(10)

# Add Summary
pdf.set_font("Arial", style='B', size=14)
pdf.cell(200, 10, "Professional Summary", ln=True, align='L')
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, summary)
pdf.ln(10)

#Education

pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "Education", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, education)


#Add linkedin
pdf.set_font("Arial","B",12)
pdf.cell(200,10,f"LinkedIn: {linkedin}",ln=True, align="c")

#Add skills

pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "Skills:", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, skills)


#lang

pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "Languages:", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, lang)


#add experience

pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "Experience:", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, experience)

# Save PDF
pdf.output("resume.pdf")

print("Resume saved as resume.pdf!")


file_name = "resume.pdf"  # Your generated PDF file

# Ask the user before deleting
delete_pdf = input("Do you want to delete the generated PDF? (yes/no): ").strip().lower()

if delete_pdf == "yes":
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"{file_name} has been deleted successfully!")
    else:
        print("Error: The file does not exist.")
else:
    print("The PDF file is saved.")