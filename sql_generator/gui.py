# We make the GUI first, becuase thats easy :P

from tkinter import *

class Gui:

	def __init__(self):
		self.window = Tk()
		self.window.title("SQL Generator")
		#icon = PhotoImage(file="resources/icon.ico")
		#window.iconbitmap(image=icon)
		self.window.iconbitmap(r'resources/icon.ico')

		self.window.mainloop()