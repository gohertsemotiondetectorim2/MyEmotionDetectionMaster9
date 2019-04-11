#import kinter as tk                # python 3
#from tkinter import font  as tkfont # python 3
import Tkinter as tk     # python 2
import tkFont as tkfont  # python 2
import Tkinter as Tk

from EmotionDetection import WordMap
from EmotionDetection import EvaluateText
from EmotionDetection import GUI
#import Welcome as welcome
import tkMessageBox
import EmotionDetection.EvaluateText
from EmotionDetection.EvaluateText import evaluate
from EmotionDetection.WordFilter import WordFilter
from math import log10
import Tkinter, Tkconstants, tkFileDialog
import codecs

from EmotionDetection.EvaluateText import evaluateWord
from EmotionDetection.EvaluateText import guessEmotion


#from pandas_ml import ConfusionMatrix
from time import strftime
# from EmotionDetection.Training import Training
#from tqdm import tqdm_gui
#import matplotlib.pyplot as plt
#import WordMap

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Emotion Detection Master")
        #self.geometry('380x500')
        self.configure(bg="lightblue")
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="roman")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, MainPage, EvaluateGUI, Training, Testing, EvaluateText):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")
        #self.show_frame("Evaluator")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def Exit(self):
        tkMessageBox.showinfo('Exiting...',"Bye-Bye...")
        app.destroy();


class HomePage(tk.Frame):
    
    #def Exit():
     #   app.destroy();
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="I Am Your Emotion Detector", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Click Me to Start", height = 1, width = 15, command=lambda: controller.show_frame("MainPage")).pack()
        #button2 = tk.Button(self, text="Evaluator", height = 1, width = 15, command=lambda: controller.show_frame("Evaluator")).pack()
        button6 = tk.Button(self, text="Exit", height = 1, width = 7, command=lambda: controller.Exit()).pack()




class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to Emotion Detection", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        # self.traningclass = Training()
        button1 = tk.Button(self, text="Training", height = 1, width = 7,command=lambda: controller.show_frame("Training")).pack()
        button2 = tk.Button(self, text="Testing", height = 1, width = 7, command=lambda: controller.show_frame("Testing")).pack()
        button3 = tk.Button(self, text="Evaluate", height = 1, width = 7, command=lambda: controller.show_frame("EvaluateText")).pack()
        button4 = tk.Button(self, text="GUI", height = 1, width = 7, command=lambda: controller.show_frame("EvaluateGUI")).pack()
        button5 = tk.Button(self, text="AppInfo", height = 1, width = 7, command=self.AppInfo).pack()
        #button10= tk.Button(self, text="MyRule", height = 1, width = 7,command= Evaluator()).pack()             
        button = tk.Button(self, text="Go to the Home page",
                           command=lambda: controller.show_frame("HomePage"))
        button.pack(side="bottom")


    def acceptance(self):
        tkinter.messagebox.askyesno("Warning","Do you want to train your application")
        if 'yes':
            tkinter.messagebox.showinfo("Information","selected yes")
        else:
             controller.show_frame("MainPage")   
    def AppInfo(self):
        tkMessageBox.showinfo('App Info', "EmotionDetection v1, sentiment analysis system operating off a multinomial Naive Bayes classififer.\n\nThere are 13 possible labels that text can be labelled as,\nthe emotions are :empty, sadness, enthusiasm, neutral, worry, surprise, love, fun, hate, happiness, boredom, relief and anger.\n\n1. Training       - Generates a WordMap using a text file and emotion value file. A word map is required for both testing and evaluation.\n\n2. Testing       - Run the system and test its accuracy by supplying correct emotion values. Also produces reports and confusion plot\n\n3. Evaluate Text - Run the system without given values. Used to evaluate input file that has not been pre-labelled.")




class Training(tk.Frame):
    
    def text_file_Button_func(self):
       
        self.filename = None
        filename = None
        self.filename = tkFileDialog.askopenfilename(parent=self,initialdir = "/",
                                                       title = "Select file",
                                                       filetypes = (("Excel files","*.csv"),("all files","*.*")))
        filename = self.filename
        self.text_file.config(state='normal')
        self.text_file.delete(0, 'end')
        self.text_file.insert(0, filename)
        return self.filename
        
    def value_file_Button_func(self):
        self.filename = None
        filename = None
        self.filename = tkFileDialog.askopenfilename(parent=self,initialdir = "/",
                                                       title = "Select file",
                                                       filetypes = (("Excel files","*.csv"),("all files","*.*")))
        filename = self.filename
        self.value_file.config(state='normal')
        self.value_file.delete(0, 'end')
        self.value_file.insert(0, filename)
        return self.filename


    def Upload(self):
        text = self.text_file.get()
        values = self.value_file.get()
        try:
            with codecs.open(text, 'r', encoding='utf-8', errors='ignore') as textFile:
            #with open(text, 'r') as textFile:
                with open(values, 'r') as valueFile:               
                    WordMap.buildWordMap('y', textFile, valueFile)
        except IOError:        
            print("File not found. Returning to main menu...\n")

        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label=tk.Label(self,text="Train the system", font=(None,15)).grid(row=0, sticky="nsew")
        label1=tk.Label(self, text="Text File", font=(None, 10)).grid(row=1, sticky="nsew")
        #label1.pack(side="left", fill="x", pady=10)
        label2=tk.Label(self, text="Value File", font=(None, 10)).grid(row=2, sticky="nsew")
        #label2.pack(side="left", fill="x", pady=10)
        self.text_file_var = tk.StringVar()
        self.text_file = tk.Entry(self,width=50, textvariable=self.text_file_var)
        self.text_file.pack()
        self.text_file.grid(row=1, column=1, sticky="nsew")
        self.value_file_var = tk.StringVar()
        self.value_file = tk.Entry(self,width=50)
        self.value_file.pack()
        self.value_file.grid(row=2, column=1, sticky="nsew")
        text_file_Button = tk.Button(self, text="Browse", font=(None, 10),height = 1, width = 7, command= self.text_file_Button_func).grid(row=1, column=2, sticky="nsew")
        Value_file_Button = tk.Button(self, text="Browse", font=(None, 10),height = 1, width = 7, command= self.value_file_Button_func).grid(row=2, column=2, sticky="nsew")


        button = tk.Button(self, text="Upload",height = 1, width=7, command= self.Upload).grid(row=3,column=2, sticky="nsew")

        button = tk.Button(self, text="Go Back", command=lambda: controller.show_frame("MainPage"),height = 1,width=7).grid(row=4, column=3, sticky="nsew")

class Testing(tk.Frame):
    
    def text_file_Button_func(self):
       
        self.filename = None
        filename = None
        self.filename = tkFileDialog.askopenfilename(parent=self,initialdir = "/",
                                                       title = "Select file",
                                                       filetypes = (("Excel files","*.csv"),("all files","*.*")))
        filename = self.filename
        self.text_file.config(state='normal')
        self.text_file.delete(0, 'end')
        self.text_file.insert(0, filename)
        return self.filename
        
    def value_file_Button_func(self):
        self.filename = None
        filename = None
        self.filename = tkFileDialog.askopenfilename(parent=self,initialdir = "/",
                                                       title = "Select file",
                                                       filetypes = (("Excel files","*.csv"),("all files","*.*")))
        filename = self.filename
        self.value_file.config(state='normal')
        self.value_file.delete(0, 'end')
        self.value_file.insert(0, filename)
        return self.filename

    def Upload(self):
        text = self.text_file.get()
        values = self.value_file.get()
        try:
            #with open(text, 'r') as textFile:
            with codecs.open(text, 'r', encoding='utf-8', errors='ignore') as textFile:
                with open(values, 'r') as valueFile:               
                    evaluate(textFile, valueFile)
        except IOError:        
            print("File not found. Returning to main menu...\n")


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label=tk.Label(self,text="Testing the system", font=(None,15)).grid(row=0, sticky="nsew")
        label1=tk.Label(self, text="Text File", font=(None, 10)).grid(row=1, sticky="nsew")
        #label1.pack(side="left", fill="x", pady=10)
        label2=tk.Label(self, text="Value File", font=(None, 10)).grid(row=2, sticky="nsew")
        #label2.pack(side="left", fill="x", pady=10)
        self.text_file_var = tk.StringVar()
        self.text_file = tk.Entry(self,width=50, textvariable=self.text_file_var)
        self.text_file.pack()
        self.text_file.grid(row=1, column=1, sticky="nsew")
        self.value_file_var = tk.StringVar()
        self.value_file = tk.Entry(self,width=50)
        self.value_file.pack()
        self.value_file.grid(row=2, column=1, sticky="nsew")
        text_file_Button = tk.Button(self, text="Browse", font=(None, 10),height = 1, width = 7, command= self.text_file_Button_func).grid(row=1, column=2, sticky="nsew")
        Value_file_Button = tk.Button(self, text="Browse", font=(None, 10),height = 1, width = 7, command= self.value_file_Button_func).grid(row=2, column=2, sticky="nsew")

        button = tk.Button(self, text="Upload",height = 1, width=7, command= self.Upload).grid(row=3,column=2, sticky="nsew")

        button = tk.Button(self, text="Go Back", command=lambda: controller.show_frame("MainPage"),height = 1,width=7).grid(row=4, column=3, sticky="nsew")

        
class EvaluateText(tk.Frame):
    
    def text_file_Button_func(self):
       
        self.filename = None
        filename = None
        self.filename = tkFileDialog.askopenfilename(parent=self,initialdir = "/",
                                                       title = "Select file",
                                                       filetypes = (("Excel files","*.csv"),("all files","*.*")))
        filename = self.filename
        self.text_file.config(state='normal')
        self.text_file.delete(0, 'end')
        self.text_file.insert(0, filename)
        return self.filename
        
    def Upload(self):
        text = self.text_file.get()
        #values = value_file.get()
        try:
            #with open(text, 'r') as textFile:
            with codecs.open(text, 'r', encoding='utf-8', errors='ignore') as textFile:
                evaluate(textFile)#, valueFile)
        except IOError:        
            print("File not found. Returning to main menu...\n")

        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label=tk.Label(self,text="Evaluate The Text", font=(None,15)).grid(row=0, sticky="nsew")
        label1=tk.Label(self, text="Text File", font=(None, 10)).grid(row=1, sticky="nsew")
        #label1.pack(side="left", fill="x", pady=10)
        #label2=tk.Label(self, text="Value File", font=(None, 10)).grid(row=2, sticky="nsew")
        #label2.pack(side="left", fill="x", pady=10)
        self.text_file_var = tk.StringVar()
        self.text_file = tk.Entry(self,width=50, textvariable=self.text_file_var)
        #self.text_file.pack()
        self.text_file.grid(row=1, column=1, sticky="nsew")
        #self.value_file_var = tk.StringVar()
        #self.value_file = tk.Entry(self,width=50)
        #self.value_file.pack()
        #self.value_file.grid(row=2, column=1, sticky="nsew")
        text_file_Button = tk.Button(self, text="Browse", font=(None, 10),height = 1, width = 7, command= self.text_file_Button_func).grid(row=1, column=2, sticky="nsew")
        #Value_file_Button = tk.Button(self, text="Browse", font=(None, 10),height = 1, width = 7, command= self.value_file_Button_func).grid(row=2, column=2, sticky="nsew")


        button = tk.Button(self, text="Upload",height = 1, width=7, command= self.Upload).grid(row=3,column=2, sticky="nsew")

        button = tk.Button(self, text="Go Back", command=lambda: controller.show_frame("MainPage"),height = 1,width=7).grid(row=4, column=3, sticky="nsew")




class EvaluateGUI(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label= tk.Label(self, text="GUI Evaluation", font=(None,15)).grid(row=0, column=0, sticky="nsew")
        label1=tk.Label(self, text="Input text:", font=(None, 10)).grid(row=1, sticky="nsew")#, pady=5)
        #label1.pack(side="left", fill="x", pady=10)
        self.v = tk.StringVar()
        self.output = tk.Label(self, textvariable=self.v, font=(None, 10)).grid(row=2, column=1)

        self.text_file_var = tk.StringVar()
        self.text_file = tk.Entry(self, font=(None, 15), width=20, textvariable=self.text_file_var)
        #self.text_file.pack()

        #self.output = tk.Label(main, textvariable=self.v, font=(None, 15))

        
        self.text_file.grid(row=1, column=1, sticky="nsew")
        
        #self.inputStr = tk.Entry(self, font=(None, 15), width=20).grid(row=1, column=1, sticky="nsew")#, pady=5)
        #self.inputStr.pack(side="left", fill="x")

        label2=tk.Label(self, text="Predicted:", font=(None, 10)).grid(row=2, column=0, sticky="nsew")
        #label2.pack(side="top", fill="x", pady=10)

        #self.v = tk.StringVar()

        #outputLabel=tk.Label(self, text="OutputText", textvariable=self.v, font=(None, 15)).grid(row=2, column=1, sticky="nsew")#, pady=5)
        

        #result=StringVar()
        #Output= tk.Label(self, textvariable=result, font=(None,15)).grid(row=2, column=1, sticky="nsew")

        #self.v = tk.StringVar()
        #self.output = tk.Label(self, textvariable=self.v, font=(None, 15)).grid(row=2, column=1, sticky="nsew")#, pady=5)
        #self.output.pack(side="left",)
        
        button1=tk.Button(self,
                  text='Clear', command=self.clearButton,
                  #command=self.clearButton,
                  font=(None, 10),height = 1, width = 7).grid(row=1, column=2, stick="nsew")#, pady=(8, 2), padx=10)
        #button1.pack()
        button2=tk.Button(self,
                  text='Predict',
                  command=self.predButton,
                  font=(None, 10),height = 1, width = 7).grid(row=2, column=2, sticky="nsew")#, pady=9, padx=20)
        #button2.pack()
        button3=tk.Button(self,
                  text='Quit',
                  #command=self.destroy,
                  font=(None, 10),height = 1, width = 7,  command=lambda: controller.show_frame("MainPage")).grid(row=3, column=2, sticky="nsew")#, pady=(2, 8), padx=10)
        #button3.pack()
        #button = tk.Button(self, text="Quit", command=lambda: controller.show_frame("PageOne"),height = 1,width=7).grid(row=4, column=3, sticky="nsew")
        button = tk.Button(self, text="Go to the Home page", command=lambda: controller.show_frame("HomePage"),height = 2).grid(row=4, column=3, sticky="nsew")
        #button.pack(side="bottom")
        #.grid(row=0, column=1, sticky="nsew", pady=10, padx=(0, 10))
        #.grid(row=1, column=1, sticky="W")
    def call(self):
        self.v.set('shiva')

    def predButton(self):
        with open("./data/Priors.csv", "r") as priorFile:
            priors = priorFile.readline().strip().split(',')[1:]
            priors = [log10(float(x)) for x in priors]
        predValues = []
        unfound = []

        wf = WordFilter()
        words = self.text_file.get()
        print "Input:", words
        words = wf.filterWords(words)

        print "Tokens:", words
        for word in words:
            try:
                values = evaluateWord(word)
            except IOError:
                print "WordMap not found. Please train system first.\n"
                raise
            if values is not None:
                predValues.append(values)
            else:
                unfound.append(word)

        predValues = map(sum, zip(*predValues))
        predProb = map(sum, zip(priors, predValues))
        predEmotion = guessEmotion(predProb)
        #if (predEmotion=="Love"):
         #       self.v.set(predEmotion,)
          #  elif(predEmotion=="Hate"):
           #     self.v.set(predEmotion)
        self.v.set(predEmotion)
        print "Unfound:", unfound
        print "Prob:", ','.join([('%.2f ') % x for x in predProb])
        print

    def clearButton(self):
        self.text_file.config(state='normal')
        self.text_file.delete(0, 'end')
        #self.text_file.insert(0, filename)
        #self.inputStr.delete(0,END)
        #self.inputStr.insert(0,"")
        return
        #self.v.delete(0,'end')
        #self.inputStr.delete(0, 'end')







         
        
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
