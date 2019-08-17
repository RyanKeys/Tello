import tkinter as tk
from controller import FrontEnd
import os
import randomcolor

APP_NAME = "Tello Controller GUI"
HEIGHT = 700
WIDTH = 800


class Application(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):

        tello_init = tk.Button(root, text="Establish a connection to the Tello:\n(Connect via Wi-Fi first)\n",
                               command=self.tello, bg=self.random_color(), fg='#000')
        tello_init.pack(side="top", padx=0, pady=20)
        code_init = tk.Button(root, text="Launch Visual Studio Code\nin your Coding directory",
                              command=self.vsc_launcher, bg=self.random_color(), fg='#000')
        code_init.pack(side='top', padx=20, pady=20)

    def tello(self):
        FrontEnd.__init__(self)

    def vsc_launcher(self):
        path = "C:/Users/skate/desktop/code"
        vsc = ' code .'
        command = (path)
        os.chdir(command)
        os.system(vsc)

    def random_color(self):
        rand_color = randomcolor.RandomColor()
        color = rand_color.generate()
        return color


root = tk.Tk()
app = Application(master=root)
app.master.title(APP_NAME)
app.mainloop()
