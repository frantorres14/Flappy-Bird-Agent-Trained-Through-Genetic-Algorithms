import numpy as np

class NeuralNetwork:
    def __init__(self, genes, input_size=5, hidden_size=2, output_size=1):
        """
        Initializes a neural network with 5 input neurons, 2 hidden neurons, and 1 output neurons.
        
        Parameters:
        genes (numpy.ndarray): An array of bits.
        """
        if not isinstance(genes, np.ndarray):
            genes = np.array(genes, dtype=np.int8)

        # Convert bit string to floating-point numbers
        float_values = self._bits_to_floats(genes)

        indice_input_hidden = input_size * hidden_size # 5 * 2 = 10
        indice_bias_hidden = indice_input_hidden + hidden_size # 10 + 2 = 12
        indice_hidden_output = indice_bias_hidden + hidden_size*output_size # 12 + 2*1 = 14

        
        # Assign weights and biases with correct shapes
        self.weights_input_hidden = float_values[:indice_input_hidden].reshape((input_size, hidden_size))
        self.bias_hidden = float_values[indice_input_hidden:indice_bias_hidden].reshape((hidden_size,))
        self.weights_hidden_output = float_values[indice_bias_hidden:indice_hidden_output].reshape((hidden_size, output_size))
        self.bias_output = float_values[indice_hidden_output:].reshape((output_size,))

    def _bits_to_floats(self, bits):
        """
        Convert a numpy array of bits into floating-point numbers between -1 and 1.
        """
        # Reshape bits into groups of 4
        bits_reshaped = bits.reshape(-1, 4)
        
        # Convert each group of 4 bits to an integer (vectorized)
        powers = np.array([8, 4, 2, 1])
        integers = np.sum(bits_reshaped * powers, axis=1)
        
        # Scale to range [-1, 1]
        float_values = integers / 8.0 - 1
        
        return float_values

    def feedforward(self, inputs):
        """
        Perform feedforward propagation through the network.
        
        Parameters:
        inputs (numpy.ndarray): Input values, should be of length 16.
        
        Returns:
        numpy.ndarray: Output values between -1 and 1.
        """
        if not isinstance(inputs, np.ndarray):
            inputs = np.array(inputs)
            
        
        # Hidden layer
        hidden = np.tanh(np.dot(inputs, self.weights_input_hidden) + self.bias_hidden)
        
        # Output layer
        outputs = np.tanh(np.dot(hidden, self.weights_hidden_output) + self.bias_output)
        
        return outputs

    def decision(self, inputs):
        output = self.feedforward(inputs)
        # Convert output to binary decision (0 or 1)
        return 1 if output[0] > 0 else 0