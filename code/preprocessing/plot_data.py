import matplotlib.pyplot as plt

def plot_data(experiment):

	plt.plot(experiment.time, experiment.x)
	plt.plot(experiment.time, experiment.y)
	plt.plot(experiment.time, experiment.z)
	plt.title('Acceleration: subject_' + experiment.subject_number + '_' + experiment.label + '_' + experiment.measurement)
	plt.legend(['a_x', 'a_y', 'a_z'])
	
	plt.show()