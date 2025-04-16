import Agente as agnt
import turtle as t
from Simulation import run_simulation
from Algen import GeneticAlgorithm as GenAlg 
import numpy as np

n_agentes = 40  # Número de agentes en la población
n_generaciones = 1000
generacion = [np.random.randint(0, 2, size=(60,)) for _ in range(n_agentes)]  # Crear población inicial

for i in range(n_generaciones):
    population = run_simulation(generacion, i)
    alg_genetico = GenAlg(population)
    generacion = alg_genetico.evolucion()
t.bye()