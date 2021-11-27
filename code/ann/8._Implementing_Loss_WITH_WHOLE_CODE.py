import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

##################################################################################
# Dense layer
##################################################################################
class Layer_Dense:
    
    # Layer initialization
    def __init__(self,n_inputs,n_neurons):
        # Initialize weights and biases
        self.weights = 0.10* np.random.rand(n_inputs,n_neurons) 
        self.biases = np.zeros((1,n_neurons))
    
    # Forward pass
    def forward(self, inputs):
        # Calculate output values from imputs, weights and biases
        self.output = np.dot(inputs, self.weights) + self.biases

##################################################################################
# ReLU activation
##################################################################################
class Activation_ReLU:
    
    # Forward pass
    def forward(self, inputs):
        # Calculate output values from imputs
        self.output = np.maximum(0, inputs)

##################################################################################
# Softmax activation
##################################################################################
class Activation_Softmax:

    # Forward pass
    def forward(self, inputs):
        # Get unnormalized probabilities
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        # Normalize them for each sample
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)

        self.output = probabilities

##################################################################################
# Common loss
##################################################################################
class Loss:
    
    # Calculates the data and regularization losses
    # given model output and ground truth values
    def calculate(self, output, y):             # output = model output ; y = intended values
        # Calculate sample losses
        sample_losses = self.forward(output, y)
        # Calculate mean losses
        data_loss = np.mean(sample_losses)
        # Return loss
        return data_loss

##################################################################################        
# Cross-entropy loss
##################################################################################
class Loss_CategoricalCrossentropy(Loss):

    # Forward pass
    def forward(self, y_pred, y_true):                                      # y_pred = model values ; y_true = training values
        # Number of samples in a batch
        samples = len(y_pred)                                               # what is total length
        # Clip data to prevent division by 0
        # Clip both sides to not drag mean towards any value
        y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7)                      # Clipping data to avoid 0 problem with LOG
        
        # Probabilities for target values -
        # only if categorical labels                                        # Here we want to operate on scalar values and hot encoded vectors dynamicly
        if len(y_true.shape) == 1:                                          # Scalar values if Yes
            correct_confidences = y_pred_clipped[range(samples), y_true]
        
        # Mask values - only for one-hot encoded labels
        elif len(y_true.shape) ==2:
            correct_confidences = np.cum(y_pred_clipped*y_true, axis =1)    # Hot encoded vectors

        # Losses
        negative_log_likehoods = -np.log(correct_confidences)
        return negative_log_likehoods

##################################################################################        
# MAIN
##################################################################################

# Create dataset
X, y = spiral_data(samples=100, classes=3)

# Create Dense layer with 2 input features and 3 output values
dense1 = Layer_Dense(2, 3)

# Create ReLU activation (to be used with Dense layer):
activation1 = Activation_ReLU()

# Create second Dense layer with 3 input features (as we take output
# of previous layer here) and 3 output values
dense2 = Layer_Dense(3, 3)

# Create Softmax activation (to be used with Dense layer):
activation2 = Activation_Softmax()

# Create loss function
loss_function = Loss_CategoricalCrossentropy()

# Perform a forward pass of our training data through this layer
dense1.forward(X)

# Perform a forward pass through activation function
# it takes the output of first dense layer here
activation1.forward(dense1.output)

# Perform a forward pass through second Dense layer
# it takes outputs of activation function of first layer as inputs
dense2.forward(activation1.output)

# Perform a forward pass through activation function
# it takes the output of second dense layer here
activation2.forward(dense2.output)

# Let's see output of the first few samples:
print(activation2.output[:5])

# Perform a forward pass through loss function
# it takes the output of second dense layer here and returns loss
loss = loss_function.calculate(activation2.output, y)

# Print loss value
print('loss:', loss)

# We get ~0.33 values since the model is random, and its average loss is also not great for
# these data, as we’ve not yet trained our model on how to correct its errors.

# Calculate accuracy from output of activation2 and targets

# calculate values along first axis
predictions = np.argmax(activation2.output, axis=1)
if len(y.shape) == 2:
    y = np.argmax(y, axis=1)
accuracy = np.mean(predictions==y)
# Print accuracy
print('acc:', accuracy)

