from tkinter import *
import tkinter as tk
from tkinter import ttk 
import tkinter.font as font
from tkinter.ttk import Label
import os
import tkinter.messagebox as messagebox
import formula
import generate
import os.path
import sys

class App(tk.Frame):
    #Widget Section
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text to Gcode Convert")
        self.root.resizable(False, False)

        self.textLabel = Label(self.root, text="Text", font=("Khmer UI",15))
        self.textEntry = tk.Entry(self.root, width=27)
        self.box = IntVar(self.root)
        self.boxCheck = tk.Checkbutton(self.root, text="Include Box Surround", variable=self.box)
        self.depthLabel = Label(self.root, text="Depth(Z):", font=("Khmer UI",15))
        self.depthEntry = tk.Entry(self.root, width=27)
        self.speedLabel = Label(self.root, text="Feedrate(F):", font=("Khmer UI",15))
        self.speedEntry = tk.Entry(self.root, width=27)
        self.submitBtn = tk.Button(self.root, text="Convert", command=self.getInput)
        self.quitBtn = tk.Button(self.root, text="Cancel", command=self.root.destroy)
        self.sizeLabel = Label(self.root, text="Font Size:", font=("Khmer UI",15))
        self.sizeInp = StringVar(self.root)
        self.sizeOpt = ttk.Combobox(self.root, state="readonly" ,width=25, textvariable=self.sizeInp)
        self.sizeOpt['values'] = ('6*10',
                                  '12*20',
                                  '18*30',
                                  '24*40',
                                  '30*50',
                                  '36*60',
                                  '42*70',
                                  '48*80',
                                  '54*90',
                                  '60*100',
                                  '66*110',
                                  '72*120',
                                  '78*130')
        self.unitInp = StringVar(self.root)
        self.unitLabel = Label(self.root, text="Unit", font=("Khmer UI", 15))
        self.unitOpt = ttk.Combobox(self.root, state="readonly", width=25, textvariable=self.unitInp)
        self.unitOpt['values'] = ('mm','cm')

            #Function for key
        def close(event):
            self.root.withdraw()
            sys.exit()
        
        self.root.bind('<Escape>', close)

        #Widget Placement
        self.textLabel.grid(row=0, column=0, sticky=W, pady=2)
        self.textEntry.grid(row=0, column=1, sticky=W, pady=2)
        self.depthLabel.grid(row=1, column=0, sticky=W, pady=2)
        self.depthEntry.grid(row=1, column=1, sticky=W, pady=2)
        self.speedLabel.grid(row=2, column=0, sticky=W, pady=2)
        self.speedEntry.grid(row=2, column=1, sticky=W, pady=2)
        self.sizeLabel.grid(row=3, column=0, sticky=W, pady=2)
        self.sizeOpt.grid(row=3, column=1, sticky=W, pady=2)
        self.sizeOpt.current(0)
        self.unitLabel.grid(row=4, column=0, sticky=W, pady=2)
        self.unitOpt.grid(row=4, column=1, stick=W, pady=2)
        self.unitOpt.current(0)
        self.boxCheck.grid(row=5, column=0, sticky=W, columnspan=2)
        self.quitBtn.grid(row=5, column=2, sticky=E)
        self.submitBtn.grid(row=5, column=3, sticky=E)
        self.root.mainloop()

    #Functions for Widget
    def getInput(self):
        inputTxt = self.textEntry.get()
        inputZ = self.depthEntry.get()
        inputF = self.speedEntry.get()
        sizeInp = self.sizeInp.get()
        unitInp = self.unitInp.get()
        if(inputTxt != "" and inputZ != "" and inputF != "" and float(inputZ) and inputF.isdigit()):
            inputTxt = inputTxt.upper()
            inputZ = float(inputZ)
            inputF = int(inputF)
            self.textEntry.delete(0, 'end')
            self.depthEntry.delete(0, 'end')
            self.speedEntry.delete(0, 'end')
            self.sizeOpt.current(0)
            try:
                file_exists = os.path.exists('output.txt')
                if(file_exists == True):
                    os.remove("output.txt")
            except:
                 messagebox.showerror("Error", "Unable to Proceed, please remove output.txt")
            #split text
            #y is always start from 0 and x will always star from left side of the character 
            formula.passText(inputTxt, 20, 0, inputF, inputZ, sizeInp, unitInp)
            if(self.box.get() == 1):
                formula.drawBox(inputZ, inputF)
            formula.finalDraw()
            generate.convert()
            messagebox.showinfo("Done!", "Please find command.nc from the source file")
            messagebox.showwarning("Please Note!", "Any duplicated command.nc will be replaced by new one, please remember to save at other location or rename it after complete.")
            self.root.destroy()
        else:
            messagebox.showerror("Error!", "Please fill all of the required field")


app = App()
