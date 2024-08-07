import turtle as t
import RedNeuronal as rn
import random 

# Clase Agente
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

    def __init__(self): 
        super().__init__() 
        self.penup() 
        self.shape("triangle") 
        self.shapesize(stretch_wid=1, stretch_len=1) 
        self.color("yellow") 
        self.speed(0) 
        self.goto(-150, 0) 
        self.vel_y = 0  
        self._genes = []
        self.fitness = 0
        self.sensores = [0, 0] 
        self.Red = rn.RedNeuronal(self.getgenes_decimal())
        self.alive = True

    def _saltar(self):
        """"
        Determina si el agente debe saltar o no basándose en la decisión de la red neuronal
        
        Returns:
        --------
        int
            Retorna 0 si la red neuronal decide no saltar, 10 si decide saltar
        """
        if self.Red.decision(self.sensores) == 0:
            return 0 
        else: 
            return 10

    def moverse(self):
        """
        Mueve al agente en el eje y
        """
        y = self.ycor()
        if self._saltar() == 0:
            self.vel_y += - 1
        else:
            self.vel_y = self._saltar()
        y += self.vel_y
        self.sety(y)  

    def primera_generacion(self):
        """
        Genera la primera generación de agentes con genes aleatorios
        """ 
        self._genes = self._generar_genes() 
        self.goto(-150, random.randint(-200, 200))
        self.Red = rn.RedNeuronal(self.getgenes_decimal())  

    def _generar_genes(self):
        """
        Genera genes aleatorios

        Returns:
        --------
        list
            Lista de bits que representan los genes del agente
        """
        genes = []
        for _ in range(0, 24): #24 alelos, 6 pesos x 4 bits
            r = random.randint(0, 1)
            genes.append(r)
        return genes
    
    def getgenes_decimal(self):
        """
        Convierte los genes en decimal

        Returns:
        --------
        list
            Lista de valores decimales que representan los genes del agente
        """
        cadena = self._genes #lista de bits
        cadena_decimal = []
        for i in range(0, len(cadena), 4):
            entero = cadena[i] * (2**3) + cadena[i + 1] * (2**2) + cadena[i + 2]*2 + cadena[i + 3]
            decimal = entero / (2**3) - 1
            cadena_decimal.append(decimal)
        return cadena_decimal
    
    def getgenes_binario(self):
        """
        Retorna los genes en binario

        Returns:
        --------
        list
            Lista de bits que representan los genes del agente
        """
        return self._genes
    
    def setgenes(self, genes): 
        """
        Modifica los genes del agente

        Parameters:
        -----------
        genes: list
            Lista de bits que representan los genes del agente
        """
        self._genes = genes

    
    def calcular_fitness(self):
        """
        Calcula la aptitud del agente
        """
        self.fitness += 0.1

    def is_alive(self):
        """
        Verifica si el agente está vivo

        Returns:
        --------
        bool
            Retorna True si el agente está vivo, False si no lo está
        """
        if (-290 <= self.ycor() <= 290) and (self.alive == True):
            return True
        else:
            return False

    def getfitness(self):
        """
        Retorna la aptitud del agente

        Returns:
        --------
        int
            Valor que representa la aptitud del agente
        """
        return self.fitness
    
    def detector_sensores(self, pipes):
        """
        Actualiza los valores de los sensores

        Parameters:
        -----------
        pipes: list
            Lista de tubos que representan los obstáculos
        """
        pipes.sort(key=lambda pipe: pipe.pipe1.xcor(), reverse = False)   
        for pipe in pipes:
            if self.xcor() - 10 < pipe.pipe1.xcor() + pipe.pipe1.ancho/2:
                if (pipe.get_punto_medio() - self.ycor()) > 0:
                    self.sensores[0] = 1
                elif (pipe.get_punto_medio() - self.ycor()) < 0:
                    self.sensores[0] = -1
                else:
                    self.sensores[0] = 0
                if pipe.is_in_area(self.xcor(), self.ycor()):
                    self.alive = False
                break

        self.sensores[1] = (self.ycor()/300)**2
        
    def aumentar_fitness(self, x):
        """
        Aumenta la aptitud del agente

        Parameters:
        -----------
        x: int
            Valor que se suma a la aptitud del agente
        """
        self.fitness += x