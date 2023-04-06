import tkinter as tk
from tkinter import messagebox

class MyGUI:

    def __init__(self):

        self.root = tk.Tk()

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

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()


    def show_message(self):

        print(self.check_state.get())

        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
           messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
      #  print(event.keysym)
      # print(event.state)

      if event.state == 20 and event.keysym == "Return":
         self.show_message()


    def on_closing(self):
       if messagebox.askyesno(title="Quit?", message="Do you really want to quit ?"):
        self.root.destroy()





MyGUI()



