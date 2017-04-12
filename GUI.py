import tkinter as tk
from PIL import ImageTk, Image
import os
import sys
import sqlite3


LARGE_FONT= ("Verdana", 12)


class GUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainMenu, OpenPage, PasswordPage,ManagePage,AddPage,DeletePage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Main Menu", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="OPEN",
                            command=lambda: controller.show_frame(OpenPage))
        button.pack()



class OpenPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="OPENPAGE", font=LARGE_FONT)
        label1.pack(pady=10,padx=10)

	path = "fp.jpg"
	img = ImageTk.PhotoImage(Image.open(path))
	panel = tk.Label(window, image = img)
        button1 = tk.Button(self, text="Menu",
                            command=lambda: controller.show_frame(MainMenu))
        button1.pack()

        button2 = tk.Button(self, text="MANAGE",
                            command=lambda: controller.show_frame(PasswordPage))
        button2.pack()

	if checker:
         label2 = tk.Label(self, text="success", font=LARGE_FONT)
         label2.pack(pady=10,padx=10)
	else:
	 label2 = tk.Label(self, text="fail", font=LARGE_FONT)
         label2.pack(pady=10,padx=10)
	

class PasswordPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PASSWORD", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Menu",
                            command=lambda: controller.show_frame(MainMenu))
        button1.pack()

        button2 = tk.Button(self, text="OK",
                            command= okBotton)
        button2.pack()
	entry = tk.Entry(app,textvariable=ment)
	entry.pack()

    def okBotton():

	if checker:
	 controller.show_frame(ManagePage)
	else:
	 tkMessageBox.showinfo("Password","Incorrect password")
	 

class ManagePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="MANAGE", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Menu",
                            command=lambda: controller.show_frame(MainMenu))
        button1.pack()

        button2 = tk.Button(self, text="Add",
                            command=lambda: controller.show_frame(AddPage))
        button2.pack()

        button3 = tk.Button(self, text="Delete",
                            command=lambda: controller.show_frame(DeletePage))
        button3.pack()
        

class AddPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ADD", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Menu",
                            command=lambda: controller.show_frame(MainMenu))
        button1.pack()
	with con:
		cur = con.cursor()
		


class DeletePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="DELETE", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Menu",
                            command=lambda: controller.show_frame(MainMenu))
        button1.pack()


con = lite.connect('database.db')
cursor = connection.cursor()
with con:
	cur = concursor()
	cur.execute("CREATE TABLE FINGER(ID INT, NAME TEXT)")
con.close()
correctPW = "buckeye"
checker = 1
app = GUI()
app.title("Fingerprint")
app.geometry("640x480")
app.mainloop()
