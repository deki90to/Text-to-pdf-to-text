from tkinter import *
from fpdf import FPDF
import PyPDF2
import img2pdf
from PIL import Image
import os

root = Tk()
root.geometry('310x150')
root['bg']='#004038'
root.title('PDF Converter')
root.resizable(False, False)


def clear_text():
   text_file_input.delete(0, END)


input_text = StringVar()

text_label = Label(root, text='Enter file name without extension', bg='#004038', fg='white')
text_label.pack()

text_file_input = Entry(root, width = 100, textvar = input_text)
text_file_input.pack()


def convert_text_file():
    try:
        text_file = input_text.get() + ".txt"

        with open(text_file, "r") as file:
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

                print("Successfully converted to pdf")
                clear_text()

        result_label.config(text="Successfully converted to .pdf")

    except FileNotFoundError:
        result_label.config(text="File not found. Please enter a valid file name.")
    except:
        result_label.config(text="An error occurred. Please check the file and try again.")

Button(root, width=80, bg='red', fg='white', relief='sunken', text='.txt > .pdf', command=convert_text_file).pack()


def convert_pdf_file():
    try:
        pdf_file = input_text.get().split('.')[0] + '.pdf'

        with open(pdf_file, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            for page_num in range(len(pdf_reader.pages)):
                text = pdf_reader.pages[page_num].extract_text()

                textfile_name = pdf_file.split(".")[0] + ".txt"
                with open(textfile_name, 'w') as outfile:
                    outfile.write(text)

            print("Successfully converted to txt")
            clear_text()

        result_label.config(text="Successfully converted to .txt")

    except FileNotFoundError:
        result_label.config(text="File not found. Please enter a valid file name.")
    except:
        result_label.config(text="An error occurred. Please check the file and try again.")

Button(root, width=80, bg='red', fg='white', relief='sunken', text='.pdf > .txt', command=convert_pdf_file).pack()


def convert_image_to_pdf():
    pict_text = input_text.get()

    extensions = ['.jpg', '.jpeg', '.png']
    
    for extension in extensions:
        try:
            img_input = pict_text + extension
            pdf_output = pict_text + '.pdf'

            image = Image.open(img_input)
            pdf_bytes = img2pdf.convert(image.filename)

            file = open(pdf_output, "wb")
            file.write(pdf_bytes)
            image.close()
            file.close()

            print("Image successfully converted to pdf file")
            result_label.config(text="Successfully converted to .pdf")
            clear_text()
            break

        except FileNotFoundError:
            result_label.config(text="File not found. Please enter a valid file name.")
        
Button(root, width=80, bg='red', fg='white', relief='sunken', text='img > .pdf', command=convert_image_to_pdf).pack()


result_label = Label(root, text="", bg='#004038', fg='white')
result_label.pack()

root.mainloop()