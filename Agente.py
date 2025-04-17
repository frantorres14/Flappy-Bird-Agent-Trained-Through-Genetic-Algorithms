import turtle as t
from redneuronal import NeuralNetwork as nn
import numpy as np

class Agente(t.Turtle):
    """
    Clase Agente que representa un agente inteligente en un juego tipo Flappy Bird.
    Esta clase hereda de Turtle y utiliza una red neuronal para tomar decisiones
    sobre cuándo saltar para evitar obstáculos.
    Atributos:
        _vel_y (float): Velocidad vertical del agente.
        _sensores (list): Lista de 5 sensores que detectan obstáculos en diferentes direcciones.
        _Red (nn): Red neuronal que procesa los datos de los sensores para tomar decisiones.
        _fitness (float): Valor que indica el desempeño del agente en el juego.
        _genes (list): Lista de 52 valores que representan los pesos de la red neuronal.
    Métodos:
        __init__(genes, x_random, y_random=0): Inicializa un nuevo agente con genes específicos en una posición.
        _saltar(): Determina si el agente debe saltar según la decisión de la red neuronal.
        moverse(): Actualiza la posición vertical del agente según su velocidad y la decisión de saltar.
        detector_sensores(pipes): Actualiza los valores de los sensores según la proximidad de las tuberías.
        is_alive(pipes): Verifica si el agente sigue vivo (no ha chocado con tuberías ni salido de los límites).
        fitness (property): Obtiene el valor de fitness del agente.
        fitness (setter): Establece el valor de fitness del agente, validando que no sea negativo.
        genes (property): Obtiene los genes del agente.
        genes (setter): Establece los genes del agente, validando que sea una lista de 52 elementos.
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
        self._sensores = [0, 0, 0, 0, 0]  
        self._Red = nn(genes)
        self._fitness = 0
        self._genes = genes

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

    def _saltar(self):
        """
        Determina si el agente debe saltar según la decisión de la red neuronal.
        La red neuronal toma como entrada los valores de los sensores y devuelve un valor
        mayor que 0 si el agente debe saltar.
        Returns:
            bool: True si el agente debe saltar, False en caso contrario.
        """
        if self._Red.decision(self._sensores) > 0:
            return True
        return False
    
    def moverse(self):
        """
        Actualiza la posición vertical del agente según su velocidad y la decisión de saltar.
        Si el agente decide saltar, se establece una velocidad vertical positiva igual a 7.
        Si no, se aplica una aceleración negativa a la velocidad vertical que aumenta 0.7 cada iteración.
        La posición vertical del agente se actualiza en función de la velocidad vertical.
        """
        if self._saltar():
            self._vel_y = 7
        else:
            self._vel_y += -0.7
        y = self.ycor() + self._vel_y
        self.sety(y)
        
    
    def detector_sensores(self, pipes):
        """
        Detecta obstáculos (tuberías) alrededor del agente utilizando sensores direccionales.
        Este método simula cinco sensores que detectan distancias a los obstáculos:
        - Sensor 0: Detecta en dirección diagonal superior derecha
        - Sensor 1: Detecta en dirección diagonal inferior derecha
        - Sensor 2: Detecta en dirección superior
        - Sensor 3: Detecta en dirección inferior
        - Sensor 4: Detecta en dirección derecha
        Las distancias se normalizan dividiendo por 100, resultando en valores entre 0.2 y 2.5,
        donde 2.5 indica que no se detectó ningún obstáculo en esa dirección dentro del rango máximo.
        Args:
            pipes (list): Lista de objetos tuberías en el juego
        Returns:
            None: Los resultados se almacenan en el atributo self._sensores
        """
        x = self.xcor()
        y = self.ycor()
        
        pipes = pipes[0:3] ## Limita la detección a las primeras 3 tuberías para optimizar el rendimiento
        self._sensores = [2.5, 2.5, 2.5, 2.5, 2.5]  # Reinicia los sensores a un valor por defecto

        # Detecta la distancia a los obstáculos en cada dirección
        for pipe in pipes:
            # Sensor 0: Diagonal superior derecha
            if self._sensores[0] == 2.5:
                for dist_sensor_positivo in range(20, 251, 10): 
                    self._sensores[0] = dist_sensor_positivo/100 
                    if pipe.is_in_area(x + dist_sensor_positivo, y + dist_sensor_positivo):
                        break
            
            # Sensor 1: Diagonal inferior derecha
            if self._sensores[1] == 2.5:
                for dist_sensor_negativo in range(20, 251, 10):
                    self._sensores[1] = dist_sensor_negativo/100
                    if pipe.is_in_area(x + dist_sensor_negativo, y - dist_sensor_negativo):
                        break
                
            # Sensor 2: Superior
            if self._sensores[2] == 2.5:
                for dist_sensor_superior in range(20, 251, 10):
                    self._sensores[2] = dist_sensor_superior/100
                    if pipe.is_in_area(x, y + dist_sensor_superior) or y + dist_sensor_superior > 300:
                        break
            
            # Sensor 3: Inferior
            if self._sensores[3] == 2.5:
                for dist_sensor_inferior in range(20, 251, 10):
                    self._sensores[3] = dist_sensor_inferior/100
                    if pipe.is_in_area(x, y - dist_sensor_inferior) or y - dist_sensor_inferior < -300:
                        break

            # Sensor 4: Derecha
            if self._sensores[4] == 2.5:
                for dist_sensor_derecho in range(20, 251, 10):
                    self._sensores[4] = dist_sensor_derecho/100
                    if pipe.is_in_area(x + dist_sensor_derecho, y):
                        break
                
    def is_alive(self, pipes):
        """
        Verifica si el agente sigue vivo (no ha chocado con tuberías ni salido de los límites).
        Args:
            pipes (list): Lista de objetos tuberías en el juego
        Returns:
            bool: True si el agente está vivo, False en caso contrario.
        """
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