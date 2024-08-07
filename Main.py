import Agente as agnt
import turtle as t
import Simulation as sim 
import Algen as alg 

n = 10
n_generaciones = 20

t.tracer(0)
texto = t.Turtle()
texto.color("black")
texto.penup()
texto.goto(-250, 270)
texto.hideturtle()

screen = t.Screen()
screen.tracer(0)
screen.title("Flappy Bird con algoritmos genéticos")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)
screen.tracer(0)  # Desactivar actualizaciones automáticas
root = t.getcanvas().winfo_toplevel()
root.resizable(False, False)

generacion = [None] * n
for i in range(n):
    generacion[i] = agnt.Agente()
    generacion[i].primera_generacion()

for i in range(n_generaciones):
    simulacion = sim.Simulation(generacion)
    texto.write("Generación: " + str(i), font=("Arial", 16, "normal"))
    simulacion.run()
    t.tracer(0)
    texto.clear()
    screen.bgcolor("lightblue")
    seleccion = alg.Seleccion(generacion)
    generacion = seleccion.do()
t.bye()