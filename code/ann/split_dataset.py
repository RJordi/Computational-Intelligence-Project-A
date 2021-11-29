import numpy as np

def split_dataset(samples_tensor, labels_array):

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


	number_of_total_data = np.shape(samples_tensor)[0] # each data entity is a step of an experiment
	
	number_of_training_data = int(0.7*number_of_total_data)
	number_of_validation_data = int(0.15*number_of_total_data)
	number_of_test_data = int(0.15*number_of_total_data)

	validation_idx = np.random.randint(0, number_of_total_data//2, size=number_of_validation_data)
	test_idx = np.random.randint(number_of_total_data//2, number_of_total_data, size=number_of_test_data)

	#print('validation idx: ', validation_idx)
	#print('test idx: ', test_idx)

	validation_tensor = samples_tensor[validation_idx]
	validation_labels = labels_array[validation_idx]
	test_tensor = samples_tensor[test_idx]
	test_labels = labels_array[test_idx]

	training_tensor = np.delete(samples_tensor, np.concatenate((validation_idx, test_idx)), 0)
	training_labels = np.delete(labels_array, np.concatenate((validation_idx, test_idx)), 0)

	#print('Shape of training tensor:', np.shape(training_tensor))
	#print('Shape of training labels:', np.shape(training_labels))


	return validation_tensor, validation_labels, test_tensor, test_labels, training_tensor, training_labels