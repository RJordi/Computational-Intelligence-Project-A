import numpy as np
import tensorflow as tf

def run_ann (validation_tensor, validation_labels, test_tensor, test_labels, training_tensor, training_labels):

	i_shape = np.shape(training_tensor)[-2:]

	model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape = i_shape), #Flatten layer allows us to get correct input format
    tf.keras.layers.Dense(50, activation = 'relu'),
    tf.keras.layers.Dense(3, activation = 'softmax')
	])

	model.compile(optimizer = 'adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

	model.fit(training_tensor, training_labels, epochs = 5, batch_size = 30)

	loss, accuracy = model.evaluate(test_tensor, test_labels, verbose=0)

	print('Loss=', loss)
	print('Accuracy=', accuracy)

	print('Showing first 10 predictions: ')
	predictions = model.predict(test_tensor[0:10])
	l = []
	for i in range(10):
		l.append(np.argmax(predictions[i]))
	print('Predicted labels: ', l)
	print('Real labels: ', test_labels[0:10])