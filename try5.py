import tkinter.messagebox
from tkinter import *
import random


def new():
    tkinter.messagebox.showinfo('Window Title', 'Well, this is new...')


root = Tk()
root.title("GUI Test Version 2")
# root.resizable(False, False)
root.geometry('{}x{}'.format(400, 400))
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Experiment...", command=new)
subMenu.add_command(label="New...", command=new)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.destroy)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=new)
toolbar = Frame(root, bg="light blue")
toolbar.pack(side=TOP, fill=X)


class App(object):
    def __init__(self, root):
        self.root = root

        self.txt_frm = Frame(self.root, width=900, height=900)
        self.txt_frm.pack(fill="both", expand=True)

        # self.button1 = Button(self.txt_frm, text="HELLO", command=self.hello_world)
        # self.button1.grid(column=0, row=2, padx=2, pady=2)
        # self.button1.bind("<Button-1>", self.drag_start)
        # self.button1.bind("<B1-Motion>", self.drag_motion)

        self.files = []  # creates list to replace your actual inputs for troubleshooting purposes
        self.button1 = []  # creates list to store the buttons ins

        for i in range(
                6):  # this just popultes a list as a replacement for your actual inputs for troubleshooting purposes
            self.files.append("Button " + str(i))

        for i in range(
                len(self.files)):  # this says for *counter* in *however many elements there are in the list files*
            # the below line creates a button and stores it in an array we can call later, it will print the value of it's own text by referencing itself from the list that the buttons are stored in
            self.button1.append(
                Button(root, text=self.files[i], command=lambda c=i: print(self.button1[c].cget("text"))))
            self.button1[i].pack()  # this packs the buttons

            self.button1[i].bind("<Button-1>", self.drag_start)
            self.button1[i].bind("<B1-Motion>", self.drag_motion)
        self.label = Label(self.txt_frm, text='')

        self.label.bind("<Button-1>", self.drag_start)
        self.label.bind("<B1-Motion>", self.drag_motion)

    def hello_world(self):
        self.label.config(text=self.update_btn_text())

    def drag_start(self, event):
        widget = event.widget
        widget.startX = event.x
        widget.startY = event.y

    def drag_motion(self, event):
        widget = event.widget
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y
        widget.place(x=x, y=y)

    def do_popup_x(self):
        x = self.button1[i].winfo_rootx()
        print("x= ", x)
        return x

    def do_popup_y(self):
        y = self.button1[i].winfo_rooty()
        print("y= ", y)
        return y

    def fire_here(self, x, y):
        print("column:{}, row:{}".format(x, y))

    def update_btn_text(self):
        x = random.randint(0, 100)
        self.label.place(x=(self.do_popup_x() + 10), y=(self.do_popup_y() - 65))
        return x


app = App(root)
root.mainloop()
