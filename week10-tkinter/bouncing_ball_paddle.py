from tkinter import Tk, Canvas
import random

class Ball:
    def __init__(self):
        self.window = Tk()
        self.window.title("BOUNCING BALL")
        self.canvas = Canvas(self.window, width=600, height=400, bg='white')
        self.canvas.pack()

        self.ball = self.canvas.create_oval(50, 50, 100, 100, fill='blue', outline='darkred')
        self.dx = 3
        self.dy = 2

        self.paddle = self.canvas.create_rectangle(250, 380, 350, 400, fill='red', outline='darkblue')
        self.paddle_speed = 8

        self.window.bind("<Left>", self.move_left)
        self.window.bind("<Right>", self.move_right)

        self.animate()

        self.window.mainloop()

    def move_left(self, event):
        position = self.canvas.coords(self.paddle)
        if position[0] > 0:
            self.canvas.move(self.paddle, -self.paddle_speed, 0)

    def move_right(self, event):
        position = self.canvas.coords(self.paddle)
        if position[2] < 600:
            self.canvas.move(self.paddle, self.paddle_speed, 0)

    def animate(self):
        position_ball = self.canvas.coords(self.ball)
        position_paddle = self.canvas.coords(self.paddle)

        # Colision with paddle
        if position_ball[3] >= position_paddle[1] and \
            ((position_ball[0] >= position_paddle[0] and position_ball[0] <= position_paddle[2]) or \
             (position_ball[2] > position_paddle[0] and position_ball[2] <= position_paddle[2])):
            self.dy = -self.dy
            self.canvas.move(self.ball, self.dx, self.dy)
        else:
            # Colision detection
            if position_ball[0] <= 0 or position_ball[2] >= 600:
                self.dx = -self.dx
            # if position_ball[1] <= 0 or position_ball[3] >= 400:
            if position_ball[1] <= 0:
                self.dy = -self.dy 
            # Check out of bounds in bottom
            if position_ball[3] >= 450:
                self.canvas.move(self.ball, self.dx, -200)

        self.canvas.move(self.ball, self.dx, self.dy)

        self.window.after(30, self.animate)



simulation = Ball()