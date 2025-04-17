import numpy as np

class NeuralNetwork:
    def __init__(self, genes, input_size=5, hidden_size=2, output_size=1):
        """
        Inicializa la red neuronal con los genes proporcionados.        
        Parametros:
            genes (numpy.ndarray): Array de genes que representan los pesos y sesgos de la red.
            input_size (int): Número de entradas a la red neuronal.
            hidden_size (int): Número de neuronas en la capa oculta.
            output_size (int): Número de salidas de la red neuronal.
        """

        float_values = self._bits_to_floats(genes) # Convertir genes en bits a valores flotantes
        # Asignar tamaños de las capas
        indice_input_hidden = input_size * hidden_size # 5 * 2 = 10
        indice_bias_hidden = indice_input_hidden + hidden_size # 10 + 2 = 12
        indice_hidden_output = indice_bias_hidden + hidden_size*output_size # 12 + 2*1 = 14

        # Inicializar pesos y sesgos a partir de los valores flotantes de los genes
        self.weights_input_hidden = float_values[:indice_input_hidden].reshape((input_size, hidden_size))
        self.bias_hidden = float_values[indice_input_hidden:indice_bias_hidden].reshape((hidden_size,))
        self.weights_hidden_output = float_values[indice_bias_hidden:indice_hidden_output].reshape((hidden_size, output_size))
        self.bias_output = float_values[indice_hidden_output:].reshape((output_size,))

    def _bits_to_floats(self, bits):
        """
        Convierte un array de bits en valores flotantes
        utilizando una representación binaria de 4 bits para cada número.
        Cada grupo de 4 bits se convierte en un número entero, que luego se normaliza
        dividiendo por 8 y restando 1.
        Esto da como resultado un rango de valores entre -1 y 0.875.
        Parametros:
            bits (numpy.ndarray): Array de bits que representan los genes. 
        Retorna:
            numpy.ndarray: Array de valores flotantes convertidos de los bits.
        """
        bits_reshaped = bits.reshape(-1, 4)
        
        powers = np.array([8, 4, 2, 1])
        integers = np.sum(bits_reshaped * powers, axis=1)
        
        float_values = integers / 8.0 - 1
        
        return float_values

    def feedforward(self, inputs):
        """
        Realiza la propagación hacia adelante de la red neuronal.
        Parametros:
            inputs (numpy.ndarray): Array de entradas a la red neuronal.
        Retorna:
            numpy.ndarray: Array de salidas de la red neuronal.
        """

        # Convertir la entrada a un array de numpy si no lo es
        if not isinstance(inputs, np.ndarray):
            inputs = np.array(inputs)
            
        # Hidden layer
        hidden = np.tanh(np.dot(inputs, self.weights_input_hidden) + self.bias_hidden)
        # Output layer
        outputs = np.tanh(np.dot(hidden, self.weights_hidden_output) + self.bias_output)
        return outputs

    def decision(self, inputs):
        """
        Toma una decisión basada en la salida de la red neuronal.
        Parametros:
            inputs (numpy.ndarray): Array de entradas a la red neuronal.
        Retorna:
            int: 1 si la salida es mayor que 0, 0 en caso contrario.
        """
        output = self.feedforward(inputs)
        return 1 if output[0] > 0 else 0