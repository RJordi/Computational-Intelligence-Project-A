##############################
### Get one instance of data (object of Data) and extract relevant information
### function: extract the motion sequence
##############################

import numpy as np
from scipy import signal

def extract_sequence (experiment): # the input experiment is an object of the class Data from read_csv.py

	success = True # success variable evaluates if the motion sequence is extracted correctly.
	
	acc_vector = np.vstack((experiment.x, experiment.y, experiment.z)).T
	
	acc_abs = np.linalg.norm(acc_vector, axis=1)

	peaks, _ = signal.find_peaks(acc_abs, height=11, distance=experiment.frequency/2)
	diff_peaks = np.diff(peaks)
	gap1  = np.argmax(diff_peaks[:20])
	gap2  = np.argmax(diff_peaks[-10:])
	gap2  = int(gap2 + np.shape(diff_peaks)-10)

	experiment.time = experiment.time[peaks[gap1+1]:peaks[gap2]]
	experiment.x = acc_vector[peaks[gap1+1]:peaks[gap2]][:,0]
	experiment.y = acc_vector[peaks[gap1+1]:peaks[gap2]][:,1]
	experiment.z = acc_vector[peaks[gap1+1]:peaks[gap2]][:,2]

	if len(experiment.time) == 0:
		success = False
	elif experiment.time[-1] - experiment.time[0] < 5:
		success = False

	return success