from tkinter import Tk, Canvas

class Ball:
    def __init__(self):
        self.window = Tk()
        self.window.title("BOUNCING BALL")
        self.canvas = Canvas(self.window, width=600, height=400, bg='white')
        self.canvas.pack()

        self.ball = self.canvas.create_oval(50, 50, 100, 100, fill='blue', outline='darkred')
        self.dx = 3
        self.dy = 2

        self.animate()

        self.window.mainloop()

    def animate(self):
        position = self.canvas.coords(self.ball)

        # Colision detection
        if position[0] <= 0 or position[2] >= 600:
            self.dx = -self.dx
        if position[1] <= 0 or position[3] >= 400:
            self.dy = -self.dy 

        self.canvas.move(self.ball, self.dx, self.dy)

        self.window.after(30, self.animate)



simulation = Ball()