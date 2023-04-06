import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("First GUI")

label = tk.Label(root, text="This is a title", font=('ariel',15))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('ariel', 13))
textbox.pack()


#myInput = tk.Entry(root)
#myInput.pack(padx = 10)

#myButton = tk.Button(root, text="Button", font=('ariel', 15))
#myButton.pack(padx=10, pady=10)


frame = tk.Frame(root)

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

btn1 = tk.Button(frame, text='1', font=('ariel', 15 ))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2= tk.Button(frame, text='2', font=('ariel', 15 ))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(frame, text='3', font=('ariel', 15 ))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)


frame.pack(fill='x')




root.mainloop()
