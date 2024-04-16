from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        
      
    def up(self) :
        x = self.xcor()
        new_y = self.ycor() + 20
        self.goto(x, new_y)
    def down(self):
        x = self.xcor()
        new_y = self.ycor() - 20
        self.goto(x, new_y)
        
            