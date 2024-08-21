#main function to start the application
from tkinter import *
from tkinter.ttk import Combobox  #
from PIL import ImageTk
class CircketScore :
    def __init__(self, rootWindow):
        self.rootWindow = rootWindow
        self.rootWindow.title('LIVE CIRCKET SCORE')
        self.rootWindow.geometry('1600x1000')
        self.bg =ImageTk.PhotoImage(file="circ.jpg")
        bg = Label(self.rootWindow, image = self.bg).place(x=0,y=0)
def main():
    rootWindow = Tk()
    obj = CircketScore(rootWindow)
    rootWindow.mainloop()
    
if __name__== '__main__':
    main()
