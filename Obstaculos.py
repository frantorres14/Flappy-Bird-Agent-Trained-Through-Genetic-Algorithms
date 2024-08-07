import turtle

class Pipe:
    def __init__(self, y):
        self.pipe1 = turtle.Turtle()
        self.pipe2 = turtle.Turtle()
        self.pipe1.shape("square")
        self.pipe2.shape("square")
        self.pipe1.color("green")
        self.pipe2.color("green")
        self.pipe1.alto = 400
        self.pipe1.ancho = 100
        self.pipe2.alto = 400
        self.pipe2.ancho = 100
        self.pipe1.shapesize(stretch_wid=self.pipe1.alto/20, stretch_len= self.pipe1.ancho/20)
        self.pipe2.shapesize(stretch_wid=self.pipe2.alto/20, stretch_len= self.pipe2.ancho/20)
        self.pipe1.penup()
        self.pipe2.penup()
        self.pipe1.speed(0)
        self.pipe2.speed(0)
        self.pipe1.setx(450)
        self.pipe2.setx(450)
        self.pipe1.sety(y + 270)
        self.pipe2.sety(y - 270)
        self.punto_medio = y
        self.pipe1.x1 = 0
        self.pipe1.y1 = 0
        self.pipe1.x2 = 0
        self.pipe1.y2 = 0
        self.pipe2.x1 = 0
        self.pipe2.y1 = 0
        self.pipe2.x2 = 0
        self.pipe2.y2 = 0

    def mover(self):
        self.pipe1.setx(self.pipe1.xcor() - 4)
        self.pipe2.setx(self.pipe2.xcor() - 4)
        self.pipe1.x1 = self.pipe1.xcor() - self.pipe1.ancho/2
        self.pipe1.y1 = self.pipe1.ycor() + self.pipe1.alto/2
        self.pipe1.x2 = self.pipe1.xcor() + self.pipe1.ancho/2
        self.pipe1.y2 = self.pipe1.ycor() - self.pipe1.alto/2
        self.pipe2.x1 = self.pipe2.xcor() - self.pipe2.ancho/2
        self.pipe2.y1 = self.pipe2.ycor() + self.pipe2.alto/2
        self.pipe2.x2 = self.pipe2.xcor() + self.pipe2.ancho/2
        self.pipe2.y2 = self.pipe2.ycor() - self.pipe2.alto/2

    def is_out(self):
        if self.pipe2.xcor() < -450:
            self.pipe1.clear()
            self.pipe2.clear()
            self.pipe1.hideturtle()
            self.pipe2.hideturtle()
            return True
        
    def is_in_area(self, x, y):
        if (self.pipe1.x1 < x + 10 < self.pipe1.x2 and self.pipe1.y2 < y + 10 < self.pipe1.y1) or \
            (self.pipe1.x1 < x - 10 < self.pipe1.x2 and self.pipe1.y2 < y + 10 < self.pipe1.y1) or \
           (self.pipe2.x1 < x + 10< self.pipe2.x2 and self.pipe2.y2 < y - 10 < self.pipe2.y1) or \
            (self.pipe2.x1 < x - 10 < self.pipe2.x2 and self.pipe2.y2 < y - 10 < self.pipe2.y1):
            return True
        else:
            return False
        
    def get_punto_medio(self):
        return self.punto_medio