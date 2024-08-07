import Agente as agnt
import random
import RedNeuronal as rn

class Seleccion:
    def __init__(self, generacion):
        self.len_genes = len(generacion[0].getgenes_binario())
        self.n_agentes = len(generacion) 
        self.suma_fitness = sum([agente.getfitness() for agente in generacion])
        self.agentes_ordenados = sorted(generacion, key=lambda agente: agente.getfitness(), reverse=True)
        self.izq = [self.agentes_ordenados[i] for i in range(self.n_agentes) if i % 2 != 0]
        #esto se ordenan en reversa para poder usar .remove en 
        self.der = [self.agentes_ordenados[i] for i in reversed(range(self.n_agentes)) if i % 2 == 0]
        self.nextgeneration = []

    '''
    def _sumacuadrada(self, generacion):
        suma = 0
        for agente in generacion:
            fit = agente.getfitness()
            suma += fit**2
        return suma
    '''
    #Seleccion por principio de Bateman
    def _seleccion(self):
        # mientras que la siguiente generacion no tenga el numero de agentes que se requieren
        while len(self.nextgeneration) < self.n_agentes:
            # se selecciona un agente de la izquierda y uno de la derecha
            l_derecha = self.der.copy()
            # se recorre la lista de agentes de la izquierda
            for agente_izq in self.izq:
                for agente_der in reversed(l_derecha):
                    prob = (agente_der.getfitness())/(self.suma_fitness)
                    if random.random() < prob :
                        self.nextgeneration.append(self._cruza(agente_izq, agente_der))
                        l_derecha.remove(agente_der)
                        
        return self.nextgeneration[:self.n_agentes]

    def _cruza(self, agente_izq, agente_der):
        hijo = agnt.Agente()
        cadena = []
        genes_izq = agente_izq.getgenes_binario()
        genes_der = agente_der.getgenes_binario()
        for i in range(0, self.len_genes, 4):
            punto = random.randint(1,3)
            cadena.extend(genes_izq[i:i+punto] + genes_der[i + punto: i+4])
        hijo.setgenes(cadena)
        hijo.goto(-150, random.randint(-200, 200))
        hijo.Red = rn.RedNeuronal(hijo.getgenes_decimal()) 
        return hijo

    def do(self):
        return self._seleccion()
    
 