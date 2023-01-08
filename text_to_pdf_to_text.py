from tkinter import *
from fpdf import FPDF
import PyPDF2

def convert_file(file):
    pdf = FPDF()
    pdf.add_page()

    for text in file:
        if len(text) <= 20:
            pdf.set_font("Arial","B",size=18) # For title text
            pdf.cell(w=200,h=10,txt=text,ln=1,align="C")
        else:
            pdf.set_font("Arial",size=15) # For paragraph text
            pdf.multi_cell(w=0,h=10,txt=text,align="L")

    pdf.output(f"{file.name.split('.')[0]}.pdf")
    print("Successfully converted!")

root = Tk()
root.geometry('310x100')
root['bg']='#004038'
root.title('PDF Converter')
root.resizable(False, False)

input_txt_file = StringVar()

txt_file_label = Label(root, text='Enter the name of the text file you want to convert to PDF', bg='#004038', fg='white').pack()
get_txt_file_input = Entry(root, width = 100, textvar = input_txt_file)
get_txt_file_input.pack()

def convert_text_file():
    file_name = input_txt_file.get() + ".txt"
    try:
        with open(file_name, "r") as file:
            convert_file(file)
        result_label.config(text="Successfully converted!")
    except FileNotFoundError:
        result_label.config(text="File not found. Please enter a valid file name.")
    except:
        result_label.config(text="An error occurred. Please check the file and try again.")

Button(root, width=80, bg='red', fg='white', relief='sunken', text='Convert', command=convert_text_file).pack()
result_label = Label(root, text="", bg='#004038', fg='white')
result_label.pack()

root.mainloop()
