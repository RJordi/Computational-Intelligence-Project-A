import numpy as np
from sklearn.model_selection import StratifiedKFold
#from sklearn.model_selection import KFold
from sklearn import metrics
import tensorflow as tf

def run_ann(samples_tensor, labels_array, subjects_array):
	
	# Encode labels into numbers (needed for model.fit function)
	for i in range(len(labels_array)):
		label = labels_array[i]
		if label == 'downstairs':
			labels_array[i] = 0
		if label == 'normal':
			labels_array[i] = 1
		if label == 'upstairs':
			labels_array[i] = 2
	labels_array = labels_array.astype(int)
	

	kf = StratifiedKFold(10, shuffle=True, random_state=42) # Use for KFold classification

	oos_y = []
	oos_pred = []
	fold = 0
	for train, test in kf.split(subjects_array, labels_array):
		fold+=1
		print('Fold ', fold)
		    
		x_train = samples_tensor[train]
		y_train = labels_array[train]
		#print('y_train: ', y_train)
		print('Number of downstairs: ', np.count_nonzero(y_train == 0))
		print('Number of normal: ', np.count_nonzero(y_train == 1))
		print('Number of upstairs: ', np.count_nonzero(y_train == 2))
		x_test = samples_tensor[test]
		y_test = labels_array[test]
		print(np.shape(x_train))
		print(np.shape(x_test))

		i_shape = np.shape(x_train)[-2:]

		model = tf.keras.models.Sequential([
		tf.keras.layers.Flatten(input_shape = i_shape), #Flatten layer allows us to get correct input format
		tf.keras.layers.Dense(50, activation = 'relu'),
		tf.keras.layers.Dense(3, activation = 'softmax')
		])

		model.compile(optimizer = 'adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

		model.fit(x_train, y_train, validation_data=(x_test,y_test), epochs = 10, batch_size = 30)

		loss, accuracy = model.evaluate(x_test, y_test, verbose=0)

		print('Loss=', loss)
		print('Accuracy=', accuracy)

		print('Showing first 10 predictions: ')
		predictions = model.predict(x_test[0:10])
		l = []
		for i in range(10):
			l.append(np.argmax(predictions[i]))
		print('Predicted labels: ', l)
		print('Real labels: ', y_test[0:10])


		pred = model.predict(x_test)
		oos_y.append(y_test)
		# raw probabilities to chosen class (highest probability)
		pred = np.argmax(pred, axis=1)
		oos_pred.append(pred)

		# Measure this fold's accuracy
		score = metrics.accuracy_score(y_test, pred)
		print(f"Fold score (accuracy): {score}")

	# Build the oos prediction list and calculate the error.
	oos_y = np.concatenate(oos_y)
	oos_pred = np.concatenate(oos_pred)

	score = metrics.accuracy_score(oos_y, oos_pred)
	print(f"Final score (accuracy): {score}")



