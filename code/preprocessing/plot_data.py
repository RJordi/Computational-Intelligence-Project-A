import matplotlib.pyplot as plt

def plot_data(experiment):

	plt.plot(experiment.time, experiment.x)
	#plt.plot(experiment.time, experiment.y)
	#plt.plot(experiment.time, experiment.z)
	plt.show()