##############################
### Read data from one experiment (i.e. accelerometer data from one folder inside "Smartphone1")
### class: Data
##############################

from os import path
import pandas as pd


class Data:
	def __init__(self, subject_num, label, measurement):
		self.subject_number = str(subject_num)
		self.label = label
		self.measurement = measurement

		datapath = path.join(path.dirname(path.realpath(__file__)), 'data/Smartphone1')
		self.exp_path = datapath + '/subject' + str(subject_num) + '_' + label + measurement + '/Accelerometer.csv'

	def extract_csv(self):
		df = pd.read_csv(self.exp_path)
		self.time = df[df.keys()[0]]
		self.x = df[df.keys()[1]]
		self.y = df[df.keys()[2]]
		self.z = df[df.keys()[3]]
		self.frequency = len(df)/self.time[len(df)-1] #frequency of data in Hz (s^-1)

		# NOTE: due to the rotation of the phone, initially we don't know if the data
		# of a certain coordinate really corresponds to that coordinate.
		# After rotating (PCA), the data from each coordinate will be correctly correlated. 