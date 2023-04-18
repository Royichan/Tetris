from tkinter import *
from Tetris import Tetris

class UserInterface:

    def __init__(self):
        self.window = Tk()
        self.window.geometry("500x500")

    def LoginPage(self):
        username = Label(self.window, text="Username : ")
        usernameEntry = Entry(self.window)
        password = Label(self.window, text="Password : ")
        passwordEntry = Entry(self.window)

        username.grid(row=0, column=0)
        usernameEntry.grid(row=0, column=1)
        password.
        passwordEntry.
        
        loginButton = Button(self.window, text="Login")
        signInButoon = button = Button(self.window, text="Sign In")
        loginButton.
        signInButoon.

        if False:
            game = Tetris()
            game.main_menu()

        self.window.mainloop()

    def SignInPage(self):
        pass        