
import Tkinter as tk


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

        button2 = tk.Button(self, text="MANAGE",
                            command=lambda: controller.show_frame(PasswordPage))
        button2.pack()


class OpenPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="OPENPAGE", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Menu",
                            command=lambda: controller.show_frame(MainMenu))
        button1.pack()



class PasswordPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PASSWORD", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Menu",
                            command=lambda: controller.show_frame(MainMenu))
        button1.pack()

        button2 = tk.Button(self, text="OK",
                            command=lambda: controller.show_frame(ManagePage))
        button2.pack()


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



class DeletePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="DELETE", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Menu",
                            command=lambda: controller.show_frame(MainMenu))
        button1.pack()




app = GUI()
app.geometry("640x480")
app.mainloop()
