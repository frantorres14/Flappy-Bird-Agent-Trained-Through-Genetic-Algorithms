import random
import turtle as t
import Obstaculos as obst
from Agente import Agente
from numpy import random

def run_simulation(poblacion, generacion_i, max_counter=1000):
    """
    Ejecuta la simulación de Flappy Bird con los agentes y obstáculos.

    Parámetros:
    ----------
    poblacion: list
        Lista de genes que representan a los agentes de la generación actual.
    generacion_i: int
        Número de generación actual.
    max_counter: int, opcional
        Número máximo de iteraciones antes de finalizar la simulación (por defecto 1000).
    """
    # Configuración inicial de la pantalla
    screen = t.Screen()
    screen.tracer(0) 
    screen.title(f"Flappy Bird con Algoritmo Genetico")
    screen.bgcolor("lightblue")
    screen.setup(width=800, height=600)

    # Crear texto para mostrar la generación
    texto = t.Turtle()
    texto.color("black")
    texto.penup()
    texto.goto(-250, 270)
    texto.hideturtle()

    # Crear agentes a partir de la población
    agentes = [Agente(genes, random.randint(-100, 100), random.randint(-200, 200)) for genes in poblacion]
    population = []
    for agente in agentes:
        agente.showturtle()  # Asegurarse de que los agentes sean visibles

    # Crear lista de obstáculos
    pipes = []
    counter = 0

    # Bucle principal de la simulación
    while True:
        # Mostrar la generación actual
        screen.update()
        texto.clear()

        # Crear nuevos tubos cada cierto tiempo
        if counter % 80 == 0:
            y = random.randint(-150, 150)
            par_tubos = obst.Pipe(y)
            pipes.append(par_tubos)

        # Mover tubos y eliminar los que salen de la pantalla
        for pipe in pipes:
            pipe.mover()
            if pipe.is_out():
                pipes.remove(pipe)

        # Actualizar agentes
        all_dead = True
        for agente in agentes:
            agente.detector_sensores(pipes)
            agente.moverse()
            agente.fitness += 1
            distance_to_center = abs(agente.ycor())
            agente.fitness += 0.1 * (1 - distance_to_center/300)
            if agente.is_alive(pipes):  # Si el agente está vivo
                all_dead = False    
            else:  # Si el agente está muerto
                agente.hideturtle()
                population.append({'genes': agente.genes, 'fitness': agente.fitness})
                agentes.remove(agente)

        # Si todos los agentes están muertos, salir del bucle
        #if all_dead or counter >= max_counter:
        if all_dead:
            # En lugar de limpiar toda la pantalla, solo oculta los elementos
            for pipe in pipes:
                pipe.pipe1.hideturtle()
                pipe.pipe2.hideturtle()
            for agente in agentes:
                agente.hideturtle()
            texto.clear()
            break

        counter += 1
        texto.write(f"Generación: {generacion_i}", font=("Arial", 16, "normal"))
        t.ontimer(None, 1) # Evitar que la pantalla se actualice demasiado rápido

    # Limpiar texto al final de la simulación
    texto.clear()

    sobrevivientes = [{'genes': agente.genes, 'fitness': agente.fitness} for agente in agentes]
    population.extend(sobrevivientes)  # Agregar sobrevivientes a la población

    return population
