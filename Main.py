import Agente as agnt
import turtle as t
from Simulation import run_simulation
from Algen import GeneticAlgorithm as GenAlg 
import numpy as np
 

screen = t.Screen()  # Crear una nueva pantalla de turtle

n_agentes = 40  # Número de agentes en la población
n_generaciones = 100 # Número de generaciones a simular
generacion = [np.random.randint(0, 2, size=(60,)) for _ in range(n_agentes)]  # Crear población inicial

# Ejecutar la simulación para cada generación
for i in range(n_generaciones):
    population = run_simulation(generacion, i, screen=screen)  # Ejecutar la simulación con la población generada
    alg_genetico = GenAlg(population) # Crear instancia del algoritmo genético
    generacion = alg_genetico.evolucion() # Evolucionar la población y obtener la nueva generación
t.bye()