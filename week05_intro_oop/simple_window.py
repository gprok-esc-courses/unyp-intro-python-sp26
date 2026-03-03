from tkinter import Tk, Button, Label, Entry

def button_clicked():
    name = entry.get()
    print(name)
    message = f"Hello {name}!"
    label.configure(text=message)

window = Tk()

window.title('My Window')

window.geometry("500x300")

entry = Entry(window)
entry.grid(row=0, column=0)

button = Button(window, text='Submit', command=button_clicked)
button.grid(row=1, column=0)

label = Label(window, text="Type your name and click the button")
label.grid(row=2, column=0)

window.mainloop()