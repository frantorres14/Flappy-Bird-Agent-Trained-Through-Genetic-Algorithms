import numpy as np
import random

class GeneticAlgorithm:
    def __init__(self, population):
        """
        Inicializa el algoritmo genético con una lista de individuos.
        

        """
        self.population = population
        
    def ordenar_poblacion(self):
        """
        Ordena la población de individuos por su fitness.
        """
        self.population = sorted(self.population, key=lambda individuo: individuo['fitness'], reverse=True)
        return self.population
    
    def seleccion_ruleta(self):
        """
        Selecciona dos individuos de la población utilizando el método de la ruleta.
        """
        total_fitness = sum(individuo['fitness'] for individuo in self.population)
        probabilidades = [individuo['fitness'] / total_fitness for individuo in self.population]
        seleccionados = np.random.choice(self.population, 2, p=probabilidades, replace=False)
        return seleccionados
    
    def seleccion_torneo(self, p=0.2):
        """
        Selecciona dos individuos de la población utilizando el método del torneo.
        
        Parameters:
        p (float): Proporción de individuos a seleccionar.
        """
        n = int(p * len(self.population))
        seleccionados = np.random.choice(self.population, n, replace=False)
        seleccionados = sorted(seleccionados, key=lambda individuo: individuo['fitness'], reverse=True)
        return seleccionados[:2]
    
    def cruce_un_punto(self, padre1, padre2):
        """
        Realiza el cruce de un punto entre dos padres."
        """
        punto_cruce = np.random.randint(1, len(self.population)-1)
        hijo = padre1['genes'][:punto_cruce] + padre2['genes'][punto_cruce:]
        return hijo
    
    def cruce_dos_puntos(self, padre1, padre2):
        """
        Realiza el cruce de dos puntos entre dos padres."
        """
        punto_cruce1, punto_cruce2 = sorted(random.sample(range(1,len(self.population)-1), 2))
        
        hijo = np.concatenate((padre1['genes'][:punto_cruce1], padre2['genes'][punto_cruce1:punto_cruce2], padre1['genes'][punto_cruce2:]))
        return hijo
    
    def mutacion(self, genes, probabilidad):
        """
        Realiza la mutación de un gen con una cierta probabilidad.
        """
        if np.random.rand() < probabilidad:
            i = np.random.randint(0, len(genes))
            genes[i] = 1 - genes[i]
        return genes
    
    def evolucion(self, metodo_seleccion='torneo', metodo_cruce='dos_puntos', probabilidad_mutacion=0.01):
        """
        Realiza una generación de evolución de la población."""
        nueva_poblacion = []
        
        if metodo_seleccion == 'ruleta':
            seleccion = self.seleccion_ruleta
        elif metodo_seleccion == 'torneo':
            seleccion = self.seleccion_torneo
        else:
            raise ValueError("Método de selección no válido")
        
        if metodo_cruce == 'un_punto':
            cruce = self.cruce_un_punto
        elif metodo_cruce == 'dos_puntos':
            cruce = self.cruce_dos_puntos
        else:
            raise ValueError("Método de cruce no válido")
        
        for _ in range(len(self.population)):
            padre1, padre2 = seleccion(p=0.2)
            hijo = cruce(padre1, padre2)
            hijo= self.mutacion(hijo, probabilidad_mutacion)            
            nueva_poblacion.append(hijo)
        
        return nueva_poblacion