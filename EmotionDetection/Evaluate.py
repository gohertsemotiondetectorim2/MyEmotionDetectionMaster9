from Tkinter import *
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import Tkinter as tk
import tkMessageBox
from EmotionDetection import WordMap
from EmotionDetection import EvaluateText
from EmotionDetection import GUI
#import pdb

#from Tkinter import messagebox
answer = ' ' 
class Evaluate():
    def __init__(self):
        window = Tk()
        window.lift()
        window.focus_force()

        window.title("Evaluate testing data")
     
        window.geometry('500x300')
         
        lbl_text = Label(window, text="Text File")
         
        lbl_text.grid(column=1, row=1)
         
        txt_file = Entry(window,width=50)
         
        txt_file.grid(column=2, row=1)
         
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
            answer = self.MessageBox(window=window)
            text = txt_file.get()
            
            if answer=='yes' and text != '':
                window.destroy()
                try:
                    with open(text, 'r') as textFile:             
                            EvaluateText.evaluate(textFile)
                            
                            
                except IOError:

                        MsgBox = tkMessageBox.showinfo('Error','File not found. Returning to main menu',parent=window)
                        

        btn3 = Button(window, text="Submit", command=button2)
             
        btn3.grid(column=2, row=3)

    def MessageBox(self,window):
        #global answer   
        MsgBox = tkMessageBox.askquestion ('Data Upload','Are you sure you want to upload the data?',parent=window)
        if MsgBox == 'yes':
           answer = MsgBox
           return answer
        else:
           tkMessageBox.showinfo('Return','You will now return to the application screen')
           
        window.mainloop()
        
            

        
 

