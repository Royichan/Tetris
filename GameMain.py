from tkinter import *
from pages import StartPage as sp

if __name__ == "__main__":
    game = Tk()
    game.geometry("500x500")
    mainContainer = Frame(game,height=500,width=500)
    mainContainer.pack(fill=BOTH,expand=TRUE,side=TOP)
    startPage = sp.StartPage()
    game.mainloop()