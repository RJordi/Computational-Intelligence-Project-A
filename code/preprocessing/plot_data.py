import matplotlib.pyplot as plt

def plot_experiment_data(experiment):

	plt.plot(experiment.time, experiment.x)
	plt.plot(experiment.time, experiment.y)
	plt.plot(experiment.time, experiment.z)
	plt.title('Acceleration: subject_' + experiment.subject_number + '_' + experiment.label + '_' + experiment.measurement)
	plt.legend(['a_x', 'a_y', 'a_z'])
	
	plt.show()


def plot_sampled_data(sample):

	for i in range(len(sample.x)):
		plt.plot(sample.x[i])
		#plt.plot(sample.y[i])
		#plt.plot(sample.z[i])
	plt.title('Sampled data for: subject_' + sample.title)
	
	plt.show()


def plot_resampled_data(sample_list):

	for sample in sample_list:
		#print('Number of steps:', sample.number_of_steps)
		#print('Number of data points per step:',sample.number_of_data_points_in_one_step)

		plot_sampled_data(sample)