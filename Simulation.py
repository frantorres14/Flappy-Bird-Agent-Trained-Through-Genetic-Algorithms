import random
import turtle as t
import Obstaculos as obst

class Simulation:
    def __init__(self, generacion):
        self.generacion = generacion
        self.pipes = []
        self.counter = 0
    
    def run(self):

        while True:


            if self.counter == 1000:
                all_dead = True # Bandera para saber si todos los agentes están muertos
            else:
                all_dead = False

            if all_dead:
                t.clearscreen()
                break

            t.Screen().update() # Actualizar pantalla

            # Crear tubos
            if self.counter%80 == 1:
                y = random.randint(-150, 150)
                par_tubos = obst.Pipe(y)
                self.pipes.append(par_tubos)

            # Mover tubos
            for pipe in self.pipes:
                pipe.mover()
                if pipe.is_out():
                    self.pipes.remove(pipe) # Eliminar tubos que salen de la pantalla
                    for agente in self.generacion:
                        if agente.is_alive():
                            agente.aumentar_fitness(2)

            # actualizar agentes
            all_dead = True # Bandera para saber si todos los agentes están muertos
            for agente in self.generacion:
                if agente.is_alive(): # Si el agente está vivo se actualiza
                    #print(agente.sensores[0], agente.sensores[1])
                    all_dead = False
                    agente.detector_sensores(self.pipes)
                    agente.moverse()
                    agente.calcular_fitness()
                else: # Si el agente está muerto se elimina
                    agente.hideturtle()

            

            self.counter += 1 
            t.ontimer(None, 5)

 