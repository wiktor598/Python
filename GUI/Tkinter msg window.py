import tkinter as tk
from tkinter import messagebox

class MyGUI:

    def __init__(self):

        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)  #Main Menu nav bar

        self.Home = tk.Menu(self.menubar, tearoff=0) #adds 'Home' element to object

        self.Home.add_command(label='Close', command=self.on_closing) # adds close option to 'Home' element
        self.Home.add_separator()
        self.Home.add_command(label='Close Without Question', command=exit)
        self.Home.add_separator()
        self.Home.add_command(label='Show Message', command=self.show_message)


        self.File = tk.Menu(self.menubar, tearoff=0)

        self.File.add_command(label='Save')
        self.File.add_separator()
        self.File.add_command(label='Print')


        self.menubar.add_cascade(menu=self.Home, label='Home') #add 'Home' to nav bar
        self.menubar.add_cascade(menu=self.File, label='File') # adds 'File' to navbar
        self.root.config(menu=self.menubar)




        self.label = tk.Label(self.root, text="msg", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox =tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()


        self.check = tk.Checkbutton(self.root, text="show Messagebox", font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clearbtn = tk.Button(self.root, text="Clear", font=('Arial', 18), command= self.clear)
        self.clearbtn.pack(padx=10, pady=10)


        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()


    def show_message(self):

        print(self.check_state.get())

        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
           messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
    #print(event.keysym)
    #print(event.state)

        if event.state == 20 and event.keysym == "Return":
         self.show_message()


    def on_closing(self):
       if messagebox.askyesno(title="Quit?", message="Do you really want to quit ?"):
        self.root.destroy()

    def clear(self):
       self.textbox.delete('1.0', tk.END)





MyGUI()



