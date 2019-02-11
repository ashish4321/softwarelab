# We make the GUI first, becuase thats easy :P

#TODO
#1 change none functions
#2 Add about
#3 Add canvas and functionality
#4 Add textarea for SQL

from tkinter import *
from tkinter import ttk
import webbrowser #because help is online

def none():
	print("Wait for me to implemetnt something here")

def helpweb():
	webbrowser.open("https://soren.in")

class Gui:

	def menusetup(self): #menu
		self.menubar = Menu(self.window)
		self.filemenu = Menu(self.menubar, tearoff=0)
		self.filemenu.add_command(label="Open", command=none)
		self.filemenu.add_command(label="Save", command=none)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Exit", command=self.window.quit)
		self.sqlmenu = Menu(self.menubar, tearoff=0)
		self.sqlmenu.add_command(label="Generate SQL", command=none)
		self.helpmenu = Menu(self.menubar, tearoff=0)
		self.helpmenu.add_command(label="Help", command=helpweb)
		self.helpmenu.add_command(label="About", command=none)
		self.menubar.add_cascade(label="File", menu=self.filemenu)
		self.menubar.add_cascade(label="SQL", menu = self.sqlmenu)
		self.menubar.add_cascade(label="Help", menu=self.helpmenu)

	def framesetup(self): #frames
		self.btnframe = ttk.Frame(self.window, height=400, width=200, relief=SUNKEN)
		self.canvasframe = ttk.Frame(self.window, height=400,width=600, relief=SUNKEN)
		self.outputframe = ttk.Frame(self.window, height=200, width=800, relief=SUNKEN)
		self.btnframe.grid(row=0,column=0)
		self.canvasframe.grid(row=0,column=1)
		self.outputframe.grid(row=1,column=0, columnspan=2)

	def buttons(self):
		self.eimg = PhotoImage(file="resources/entity.png")
		self.rimg = PhotoImage(file="resources/relation.png")
		self.limg = PhotoImage(file="resources/card.png")
		self.entityb = ttk.Button(self.btnframe, width=20, image=self.eimg, command=lambda : print("clicked"))
		self.relation = ttk.Button(self.btnframe, width=20, image=self.rimg, command=lambda : print("clicked"))
		self.lineb =  ttk.Button(self.btnframe, width=20, image=self.limg, command=lambda : print("clicked"))
		self.entityb.grid(row=0, column=0, sticky='e')
		self.relation.grid(row=1, column=0)
		self.lineb.grid(row=2, column=0)

	def __init__(self):
		self.window = Tk()
		self.window.geometry('800x600')
		self.window.title("SQL Generator")
		#icon = PhotoImage(file="resources/icon.ico")
		#window.iconbitmap(image=icon)
		self.window.iconbitmap(r'resources/icon.ico')
		self.menusetup()
		self.framesetup()
		self.buttons()
		#self.canvasspace()
		#self.outputwindow()
		self.window.config(menu=self.menubar)
		self.window.resizable(False, False) #resizeable false
		self.window.mainloop()