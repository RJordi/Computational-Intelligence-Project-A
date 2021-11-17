##############################
### Get one instance of data (object of Data) and extract relevant information
### function: extract the motion sequence
##############################

### PLAYGROUND ###
from read_csv import Data
import matplotlib.pyplot as plt
import numpy as np

Td = Data(241, 'downstairs', '02') # Td stands for Trial_data
Td.extract_csv()
###	PLAYGROUND ###


def extract_sequence (experiment): # the input experiment is an object of the class Data from read_csv.py
	def plot():
		plt.plot(Td.time, Td.a_x)
		#plt.plot(Td.time, np.ones(len(Td.time))*median_x)
		plt.vlines(Td.time[time_step_idx], -20, 20, colors='green')
		plt.plot()
		plt.show()

	#median_x = Td.a_x.median()
	time_step = 0.5 
	rows_per_time_step = int(time_step//Td.frequency)
	time_step_idx = [idx for idx in range(0,len(Td.time)-1,rows_per_time_step)]

	wait_flag = False
	experiment_flag = False
	variance = 1

	'''for e in range(1,len(time_step_idx)):

		time_step_a_x = Td.a_x[time_step_idx[e-1]:time_step_idx[e]]

		if abs(max(time_step_a_x)-min(time_step_a_x)) < variance:
			wait_flag = True
			if experiment_flag == True:
				end = time_step_idx[e]
				print('end: ', end)
				break
			experiment_flag = False

		if wait_flag == True and abs(max(time_step_a_x)-min(time_step_a_x)) > variance:
			wait_flag = False
			experiment_flag = True
			start = time_step_idx[e]
			print('start: ', start)

	Td.time = Td.time[start:end]
	Td.a_x = Td.a_x[start:end]
	Td.a_y = Td.a_y[start:end]
	Td.a_z = Td.a_z[start:end]'''

	plot()








if __name__ == '__main__':
	extract_sequence(Td)