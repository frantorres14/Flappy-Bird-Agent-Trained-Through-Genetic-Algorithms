import numpy as np

class Neurona: 
    def __init__(self, tipo, pesos): 
        self.pesos = np.array(pesos)
        if tipo == "sigmoide":
            self.f_activacion = self.f_sigmoide
        elif tipo == "tanh":
            self.f_activacion = self.f_tanh
        else:
            raise NotImplementedError("La función de activación no está implementada")
    
    def f_activacion(self):
        raise NotImplementedError("f_activacion no está implementada")
    
    def f_sigmoide(self, x):
        return 1 / (1 + np.exp(-x))
    
    def f_tanh(self, x):
        return np.tanh(x)
    
    def activate(self, inputs):
        
        suma = np.dot(inputs, self.pesos) 
        return self.f_activacion(suma)


class RedNeuronal:
    def __init__(self, genes): #
        self.num_entradas = 2 # numero de sensores
        self.num_ocultas = 2 
        self.num_salidas = 1
        self.pesos = genes
        #capa oculta con dos neuronas y la capa de salida con una neurona
        self.hidden_layer = [Neurona("tanh", self.pesos[self.num_entradas*i:self.num_entradas*(i+1)]) for i in range(self.num_ocultas)]
        self.output_layer = Neurona("sigmoide", self.pesos[self.num_entradas * self.num_ocultas:])

        
    def output(self, inputs):
        # Propagación hacia adelante
        hidden_layer_outputs = [neuron.activate(inputs) for neuron in self.hidden_layer]
        final_output = self.output_layer.activate(hidden_layer_outputs)
        return final_output
    
    def decision(self, inputs):
        if self.output(inputs) >= 0.5:
            return 1
        else:
            return 0
 