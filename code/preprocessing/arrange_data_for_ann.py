import numpy as np

def arrange_data (resampled_list):

	samples_tensor = []
	labels_array = [] # change to correct value

	for i in range(len(resampled_list)):
		sample = resampled_list[i]

		# stack acceleration coordinates -> shape =(#steps, acceleration_coordinate, #data_points)
		sample_stacked = np.stack(np.array((sample.x, sample.y, sample.z)), axis=1)
		#print(np.shape(sample_stacked))

		# stack all samples vertically -> shape =(#steps, acceleration_coordinate, #data_points)
		samples_tensor.append(sample_stacked)

		# append label to labels_array FOR EACH STEP AND EACH SAMPLE
		labels_array += [sample.label]*sample.number_of_steps
	
	samples_tensor = np.vstack(samples_tensor)
	labels_array = np.asarray(labels_array)
	#print('Shape of samples tensor:', np.shape(samples_tensor))
	#print('Shape of labels array:', np.shape(labels_array))
	#print(labels_array)

	return samples_tensor, labels_array