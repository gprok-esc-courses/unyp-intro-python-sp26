from tkinter import Tk, Canvas, BOTH 

window = Tk() 
window.geometry("500x500")
window.title("Drawing Example")

canvas = Canvas(window, bg='yellow')
canvas.pack(fill=BOTH, expand=True)

canvas.create_line(10, 10, 70, 70)
canvas.create_rectangle(200, 40, 250, 90, fill='red')
canvas.create_oval(100, 100, 200, 150, outline='blue', width=3)

window.mainloop()
