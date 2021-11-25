##############################
### Read data from one experiment (i.e. accelerometer data from one folder inside "Smartphone1")
### class: Data
##############################

from os import path
import pandas as pd
import numpy as np


class Data:
	def __init__(self, subject_num, label, measurement):
		self.subject_number = str(subject_num)
		self.label = label
		self.measurement = measurement

		datapath = path.join(path.dirname(path.realpath(__file__)), 'data/Smartphone1')
		self.exp_path = datapath + '/subject' + str(subject_num) + '_' + label + measurement + '/Accelerometer.csv'

	def extract_csv(self):
		df = pd.read_csv(self.exp_path)
		self.time = df[df.keys()[0]].to_numpy()
		self.x = df[df.keys()[1]].to_numpy()
		self.y = df[df.keys()[2]].to_numpy()
		self.z = df[df.keys()[3]].to_numpy()

		if str(self.time[1])[::-1].find('.') < 5: # correct low resolution on time series
			#print('LOW RESOLUTION DATA FOUND!')
			self.time = np.linspace(0, self.time[len(df)-1] - self.time[0], len(df))

		self.frequency = len(df)/(self.time[len(df)-1] - self.time[0]) #frequency of data in Hz (s^-1)

		# CHECK FOR NaN
		#if np.isnan(self.z).any() == True:
		#	print('FOUND A NaN HERE !!')


		# NOTE: due to the rotation of the phone, initially we don't know if the data
		# of a certain coordinate really corresponds to that coordinate.
		# After rotating (PCA), the data from each coordinate will be correctly correlated. 