import turtle
import random
import Obstaculos as obst

# Configuración de la pantalla
wn = turtle.Screen()
wn.title("Flappy Bird")
wn.bgcolor("skyblue")
wn.setup(width=600, height=400)
wn.tracer(0)

counter = 0 
# Clase Bird
class Bird(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("yellow")
        self.shapesize(stretch_wid=1, stretch_len=1 )
        self.penup()
        self.speed(0)
        self.goto(-200, 0)
        self.dy = 0

    def jump(self):
        self.dy = 10

    def move(self):
        self.dy -= 1
        y = self.ycor()
        y += self.dy
        if y > 190:
            y = 190
        self.sety(y)

 


# Inicialización
bird = Bird()
wn.listen()
wn.onkeypress(bird.jump, "space")

pipes = []

# Bucle principal del juego
while True:
    wn.update()

    bird.move()

    counter += 1
    if counter == 40:
        counter = 0
        y = random.randint(-150, 150)
        tubo = obst.Pipe(y)
        pipes.append(tubo)
        counter = 0  # reset counter

    for pipe in pipes:
        pipe.mover()
        if pipe.is_out():
            pipes.remove(pipe)


    turtle.ontimer(None, 20)  # Espera 20 milisegundos
 