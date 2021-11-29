from scipy import signal
import numpy as np

def resample_data (sample_list, num_samples):

	for i in range(len(sample_list)):

		sample = sample_list[i]

		sample.x = signal.resample(sample.x, num_samples, axis=1)
		sample.y = signal.resample(sample.y, num_samples, axis=1)
		sample.z = signal.resample(sample.z, num_samples, axis=1)

		sample.number_of_steps = np.shape(sample.x)[0]
		sample.number_of_data_points_in_one_step = np.shape(sample.x)[1]

		sample_list[i] = sample

	return sample_list