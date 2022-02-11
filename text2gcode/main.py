from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter.ttk import Label
import os
import tkinter.messagebox as messagebox
import formula
import generate
import os.path

class App(tk.Frame):
    #Widget Section
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text to Gcode Convert")

        self.textLabel = Label(self.root, text="Text", font=("Khmer UI",15))
        self.textEntry = tk.Entry(self.root)
        self.boxCheck = tk.Checkbutton(self.root, text="Include Box Surround")
        self.depthLabel = Label(self.root, text="Z:", font=("Khmer UI",15))
        self.depthEntry = tk.Entry(self.root)
        self.speedLabel = Label(self.root, text="F:", font=("Khmer UI",15))
        self.speedEntry = tk.Entry(self.root)
        self.submitBtn = tk.Button(self.root, text="Convert", command=self.getInput)
        self.quitBtn = tk.Button(self.root, text="Cancel", command=self.root.destroy)

        #Widget Placement
        self.textLabel.grid(row=0, column=0, sticky=W, pady=2)
        self.textEntry.grid(row=0, column=1, sticky=W, pady=2)
        self.depthLabel.grid(row=1, column=0, sticky=W, pady=2)
        self.depthEntry.grid(row=1, column=1, sticky=W, pady=2)
        self.speedLabel.grid(row=2, column=0, sticky=W, pady=2)
        self.speedEntry.grid(row=2, column=1, sticky=W, pady=2)
        self.boxCheck.grid(row=3, column=0, sticky=W, columnspan=2)
        self.quitBtn.grid(row=3, column=2, sticky=E)
        self.submitBtn.grid(row=3, column=3, sticky=E)

        self.root.mainloop()

    #Functions for Widget
    def getInput(self):
        inputTxt = self.textEntry.get()
        inputZ = self.depthEntry.get()
        inputF = self.speedEntry.get()
        if(inputTxt != "" and inputZ != "" and inputF != "" and float(inputZ) and inputF.isdigit()):
            inputTxt = inputTxt.upper()
            inputZ = float(inputZ)
            inputF = int(inputF)
            self.textEntry.delete(0, 'end')
            self.depthEntry.delete(0, 'end')
            self.speedEntry.delete(0, 'end')
            try:
                file_exists = os.path.exists('output.txt')
                if(file_exists == True):
                    os.remove("output.txt")
            except:
                 messagebox.showerror("Error", "Unable to Proceed, please remove output.txt")
            #split text
            formula.passText(inputTxt, 29.3, 20, inputF, inputZ)
            formula.finalDraw()

            generate.convert()
            messagebox.showinfo("Done!", "Please find command.nc from the source file")
            messagebox.showwarning("Please Note!", "Any duplicated command.nc will be replaced by new one, please remember to save at other location after complete.")
            self.root.destroy()
        else:
            messagebox.showerror("Error!", "Please fill all of the required field")

app = App()
