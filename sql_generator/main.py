from gui import Gui

def main():
	maingui = Gui() #initialize the GUI instance
	maingui.errorarea.insert("0.0", "GUI initialized from main!\n")
	maingui.outputarea.insert("0.0", "Sample Output: INSERT INTO xxx VALUES (1,2,3);\n")
	maingui.window.mainloop() #the mainloop
if __name__ == '__main__':
	main()