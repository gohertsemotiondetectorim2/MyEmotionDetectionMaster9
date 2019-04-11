from Tkinter import *
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import Tkinter as tk
import tkMessageBox
from EmotionDetection import WordMap
from EmotionDetection import EvaluateText
from EmotionDetection import GUI
import pdb

#from Tkinter import messagebox
answer = ' '
class Training():
    def __init__(self):
        window = Tk()
        window.lift()
        window.focus_force()

        window.title("Upload Training data")
     
        window.geometry('500x300')
         
        lbl_text = Label(window, text="Text File")
         
        lbl_text.grid(column=1, row=1)
         
        txt_file = Entry(window,width=50)
         
        txt_file.grid(column=2, row=1)

        lbl_value = Label(window, text="Value File")
         
        lbl_value.grid(column=1, row=2)
         
        value_file = Entry(window,width=50)
         
        value_file.grid(column=2, row=2)
         
        def button1():
            window.filename = None
            filename = None
            window.filename = tkFileDialog.askopenfilename(parent=window,initialdir = "/",
                                                           title = "Select file",
                                                           filetypes = (("Excel files","*.csv"),("all files","*.*")))
            filename = window.filename
            txt_file.config(state=NORMAL)
            txt_file.delete(0, END)
            txt_file.insert(0, filename)
            
        btn1 = Button(window, text="Browse", command=button1)
         
        btn1.grid(column=3, row=1)
        

        def button2():
            window.filename = None
            filename = None
            window.filename = tkFileDialog.askopenfilename(parent=window,initialdir = "/",
                                                           title = "Select file",
                                                           filetypes = (("Excel files","*.csv"),("all files","*.*")))
            filename = window.filename
            value_file.config(state=NORMAL)
            value_file.delete(0, END)
            value_file.insert(0, filename)
             
        btn2 = Button(window, text="Browse", command=button2)
         
        btn2.grid(column=3, row=2)

        def button3():
            error = tk.StringVar()
            answer = self.MessageBox(window=window)
            text = txt_file.get()
            values = value_file.get()
            
            if answer=='yes' and text != ' ':
                window.destroy()
                try:
                    with open(text, 'r') as textFile:
                        with open(values, 'r') as valueFile:               
                            WordMap.buildWordMap('y', textFile, valueFile)
                           
                            
                except IOError:
                            MsgBox = tkMessageBox.showinfo('Error','File not found. Returning to main menu',parent=window)
                            
        btn3 = Button(window, text="Submit", command=button3)
             
        btn3.grid(column=2, row=4)

    def MessageBox(self,window):
        #global answer   
        MsgBox = tkMessageBox.askquestion ('Data Upload','Are you sure you want to upload the data?',parent=window)
        if MsgBox == 'yes':
           answer = MsgBox
           return answer
        else:
           tkMessageBox.showinfo('Return','You will now return to the application screen')
           
        window.mainloop()
        
            

        
 

