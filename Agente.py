import turtle as t
from RedNeuronal import NeuralNetwork as nn
import numpy as np

class Agente(t.Turtle):
    """
    Clase que representa al pájaro que aprende a jugar Flappy Bird

    Hereda de:
    t.Turtle: Clase de la librería Turtle que representa un objeto gráfico

    Atributos:
    ----------
    penup: método de Turtle para levantar el lápiz
    shape: método de Turtle para cambiar la forma del objeto
    shapesize: método de Turtle para cambiar el tamaño del objeto
    color: método de Turtle para cambiar el color del objeto
    speed: método de Turtle para cambiar la velocidad del objeto
    goto: método de Turtle para mover el objeto a una posición específica
    vel_y: int
        Velocidad en el eje y
    _genes: list
        Lista de bits que representan los genes del agente
    fitness: int
        valor que representa la aptitud del agente
    sensores: list
        Lista que representa los valores de los sensores, los cuales son la distancia al tubo y la altura del pájaro
    Red: RedNeuronal
        Objeto de la clase RedNeuronal que representa la red neuronal del agente
    alive: bool
        Valor booleano que indica si el agente está vivo o no

    Métodos:
    --------
    __init__(): 
        Inicializa los atributos del agente y configura la apariencia del objeto Turtle.
    _saltar():
        Determina si el agente debe saltar o no basándose en la decisión de la red neuronal
    moverse():
        Mueve al agente en el eje y
    primera_generacion():
        Genera la primera generación de agentes con genes aleatorios
    _generar_genes():
        Genera genes aleatorios
    getgenes_decimal():
        Convierte los genes en decimal
    getgenes_binario():
        Retorna los genes en binario
    setgenes():
        Modifica los genes del agente
    calcular_fitness():
        Calcula la aptitud del agente
    is_alive():
        Verifica si el agente está vivo
    getfitness():
        Retorna la aptitud del agente
    detector_sensores():
        Actualiza los valores de los sensores
    aumentar_fitness():
        Aumenta la aptitud del agente
    """

    def __init__(self, genes, x_random, y_random=0): 
        super().__init__() 
        self.penup() 
        self.shape("triangle") 
        self.shapesize(stretch_wid=1, stretch_len=1) 
        self.color((np.random.rand(), np.random.rand(), np.random.rand()/2))
        self.speed(0) 
        self.goto(-150 + x_random, y_random) 
        self._vel_y = 0  
        self._sensores = [0, 0, 0, 0, 0]  # Inicializa los sensores a un valor por defecto
        self._Red = nn(genes)
        self._fitness = 0
        self._genes = genes


    def _saltar(self):
        if self._Red.decision(self._sensores) > 0:
            return True
        return False
    
    def moverse(self):
        """
        Mueve al agente en el eje y
        """
        if self._saltar():
            self._vel_y = 7
        else:
            self._vel_y += -0.7
        y = self.ycor() + self._vel_y
        self.sety(y)
        

    
    def detector_sensores(self, pipes):
        x = self.xcor()
        y = self.ycor()
        
        # Ordena la lista de tuberías en orden ascendente según xcor
        pipes = pipes[0:3]
        self._sensores = [2.5, 2.5, 2.5, 2.5, 2.5]  # Reinicia los sensores a un valor por defecto

        # Encuentra la primera tubería que no haya pasado al agente
        for pipe in pipes:
            if self._sensores[0] == 2.5:
                for dist_sensor_positivo in range(20, 251, 10):
                    self._sensores[0] = dist_sensor_positivo/100
                    if pipe.is_in_area(x + dist_sensor_positivo, y + dist_sensor_positivo):
                        break
            
            if self._sensores[1] == 2.5:
                for dist_sensor_negativo in range(20, 251, 10):
                    self._sensores[1] = dist_sensor_negativo/100
                    if pipe.is_in_area(x + dist_sensor_negativo, y - dist_sensor_negativo):
                        break
                
            if self._sensores[2] == 2.5:
                for dist_sensor_superior in range(20, 251, 10):
                    self._sensores[2] = dist_sensor_superior/100
                    if pipe.is_in_area(x, y + dist_sensor_superior) or y + dist_sensor_superior > 300:
                        break
            
            if self._sensores[3] == 2.5:
                for dist_sensor_inferior in range(20, 251, 10):
                    self._sensores[3] = dist_sensor_inferior/100
                    if pipe.is_in_area(x, y - dist_sensor_inferior) or y - dist_sensor_inferior < -300:
                        break

            if self._sensores[4] == 2.5:
                for dist_sensor_inferior in range(20, 251, 10):
                    self._sensores[4] = dist_sensor_inferior/100
                    if pipe.is_in_area(x + dist_sensor_negativo, y):
                        break
                
    def is_alive(self, pipes):
        if len(pipes) > 1:
            for pipe in pipes:
                if (pipe.is_in_area(self.xcor() + 10, self.ycor() + 10) or
                    pipe.is_in_area(self.xcor() + 10, self.ycor() - 10) or
                    pipe.is_in_area(self.xcor() - 10, self.ycor() + 10) or
                    pipe.is_in_area(self.xcor() - 10, self.ycor() - 10)):
                    return False 
        if self.ycor() < -300 or self.ycor() > 300:
            return False
        return True
    

    @property
    def fitness(self):
        return self._fitness

    @fitness.setter
    def fitness(self, value):
        if value < 0:
            raise ValueError("El fitness no puede ser negativo")
        self._fitness = value

    @property
    def genes(self):
        return self._genes
    
    @genes.setter
    def genes(self, value):
        if not isinstance(value, list) or len(value) != 52:
            raise ValueError("Los genes deben ser una lista de 52 elementos")
        self._genes = value
    