import turtle as t
import RedNeuronal as rn
import random 

# Clase Agente
class Agente(t.Turtle):

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
        if self.Red.decision(self.sensores) == 0:
            return 0 
        else: 
            return 10

    def moverse(self): 
        y = self.ycor()
        if self._saltar() == 0:
            self.vel_y += - 1
        else:
            self.vel_y = self._saltar()
        y += self.vel_y
        self.sety(y)  

    def primera_generacion(self): 
        self._genes = self._generar_genes() 
        self.goto(-150, random.randint(-200, 200))
        self.Red = rn.RedNeuronal(self.getgenes_decimal())  

    # Generar genes aleatorios
    def _generar_genes(self):
        genes = []
        for _ in range(0, 24): #24 alelos, 6 pesos x 4 bits
            r = random.randint(0, 1)
            genes.append(r)
        return genes
    
    def getgenes_decimal(self):  
        cadena = self._genes #lista de bits
        cadena_decimal = []
        for i in range(0, len(cadena), 4):
            entero = cadena[i] * (2**3) + cadena[i + 1] * (2**2) + cadena[i + 2]*2 + cadena[i + 3]
            decimal = entero / (2**3) - 1
            cadena_decimal.append(decimal)
        return cadena_decimal
    
    def getgenes_binario(self):
        return self._genes
    
    def setgenes(self, genes):  
        self._genes = genes

    
    def calcular_fitness(self):
        self.fitness += 0.1

    def is_alive(self):
        if (-290 <= self.ycor() <= 290) and (self.alive == True):
            return True
        else:
            return False

    def getfitness(self):
        return self.fitness
    
    def detector_sensores(self, pipes):
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
        self.fitness += x