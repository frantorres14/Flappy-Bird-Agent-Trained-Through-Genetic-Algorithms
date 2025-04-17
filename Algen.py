import numpy as np
import random

class GeneticAlgorithm:
    """
    Clase que implementa un algoritmo genético para la evolución de una población de individuos.
    Cada individuo está representado por un conjunto de genes que determinan su comportamiento.
    Atributos:
        population (list): Lista de individuos que componen la población.
    Métodos:
        __init__(population): Inicializa la población de individuos.
        ordenar_poblacion(): Ordena la población de individuos por su fitness.
        seleccion_ruleta(): Selecciona dos individuos de la población utilizando el método de la ruleta.
        seleccion_torneo(p): Selecciona dos individuos de la población utilizando el método del torneo.
        cruce_un_punto(padre1, padre2): Realiza el cruce de un punto entre dos padres.
        cruce_dos_puntos(padre1, padre2): Realiza el cruce de dos puntos entre dos padres.
        mutacion(genes, probabilidad): Realiza la mutación de un gen con una cierta probabilidad.
        evolucion(metodo_seleccion, metodo_cruce, probabilidad_mutacion): Realiza una generación de evolución de la población.
    """
    def __init__(self, population):
        self.population = population
        
    def ordenar_poblacion(self):
        """
        Ordena la población de individuos por su fitness.
        La población se ordena de mayor a menor fitness.
        Returns:
            list: Población ordenada por fitness.
        """
        self.population = sorted(self.population, key=lambda individuo: individuo['fitness'], reverse=True)
        return self.population
    
    def seleccion_ruleta(self):
        """
        Selecciona dos individuos de la población utilizando el método de la ruleta.
        returns:
            list: Dos individuos seleccionados de la población.
        """
        total_fitness = sum(individuo['fitness'] for individuo in self.population)
        seleccionados = []
        
        for _ in range(2):
            ruleta = np.random.rand() * total_fitness
            suma = 0
            for individuo in self.population:
                suma += individuo['fitness']
                if suma >= ruleta:
                    seleccionados.append(individuo)
                    break
        
        return seleccionados
    
    def seleccion_torneo(self, p=0.2):
        """
        Selecciona dos individuos de la población utilizando el método del torneo.
        parametros:
        p (float): Proporción de individuos a seleccionar para el torneo.
        Returns:
            list: Dos individuos seleccionados de la población.
        """
        n = int(p * len(self.population))
        seleccionados = np.random.choice(self.population, n, replace=False)
        seleccionados = sorted(seleccionados, key=lambda individuo: individuo['fitness'], reverse=True)
        return seleccionados[:2]
    
    def cruce_un_punto(self, padre1, padre2):
        """
        Realiza el cruce de un punto entre dos padres.
        Se elige un indice al azar para dividir los genes de los padres y crear un hijo.
        Parametros:
            padre1 (dict): Primer padre.
            padre2 (dict): Segundo padre.
        Returns:
            list: Genes del hijo resultante del cruce.
        """
        punto_cruce = np.random.randint(1, len(self.population)-1)
        hijo = padre1['genes'][:punto_cruce] + padre2['genes'][punto_cruce:]
        return hijo
    
    def cruce_dos_puntos(self, padre1, padre2):
        """
        Realiza el cruce de dos puntos entre dos padres.
        Se eligen dos indices al azar para dividir los genes de los padres y crear un hijo.
        Parametros:
            padre1 (dict): Primer padre.
            padre2 (dict): Segundo padre.
        Returns:
            list: Genes del hijo resultante del cruce.
        """
        punto_cruce1, punto_cruce2 = sorted(random.sample(range(1,len(self.population)-1), 2))
        
        hijo = np.concatenate((padre1['genes'][:punto_cruce1], padre2['genes'][punto_cruce1:punto_cruce2], padre1['genes'][punto_cruce2:]))
        return hijo
    
    def mutacion(self, genes, probabilidad):
        """
        Realiza la mutación de un gen con una cierta probabilidad.
        Se elige un índice al azar y se invierte el valor del gen en ese índice.
        Parametros:
            genes (list): Genes a mutar.
            probabilidad (float): Probabilidad de mutación.
        Returns:
            list: Genes mutados.
        """
        if np.random.rand() < probabilidad:
            i = np.random.randint(0, len(genes))
            genes[i] = 1 - genes[i]
        return genes
    
    def evolucion(self, metodo_seleccion='torneo', metodo_cruce='dos_puntos', probabilidad_mutacion=0.01):
        """
        Realiza una generación de evolución de la población.
        Selecciona padres, realiza cruces y mutaciones para crear una nueva población.
        Parametros:
            metodo_seleccion (str): Método de selección ('ruleta' o 'torneo').
            metodo_cruce (str): Método de cruce ('un_punto' o 'dos_puntos').
            probabilidad_mutacion (float): Probabilidad de mutación.
        Returns:
            list: Nueva población generada.
        """
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