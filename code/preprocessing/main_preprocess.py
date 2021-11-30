##############################
### Preprocess data
### main file
##############################

import numpy as np

from read_csv import Data
import filter_data
import plot_data
import extract_motion_sequence
import normalize_and_standarize
import PCA_Transform
from segment_into_samples import Sample
import resample_all_data
import arrange_data_for_ann

def main_preprocess():

	list_of_samples = []
	minP = 10000

	# Read csv data
	for subject_num in range(150, 170):
		for label in ['downstairs', 'normal', 'upstairs']:
			for measurement in ['01', '02']:
				try:
					Exp_data = Data(subject_num, label, measurement)
					Exp_data.extract_csv()
					#print(Exp_data.time, Exp_data.x, Exp_data.y, Exp_data.z)
					#print('Frequency for subject' + str(subject_num) + '_' + label + measurement + ' is: ' + str(Exp_data.frequency))
				except:
					#print('Data for subject' + str(subject_num) + '_' + label + measurement + ' is not available.')
					continue
					# another option would be to put the try except clauses in the class function extract_csv()
					# and when entering the except case we create a boolean attribute called self.available with False value

				try:

		# Filter data
					filter_data.filter_data(Exp_data)

		# Extract frequency
					if not extract_motion_sequence.extract_sequence(Exp_data):
						#print('Motion sequence not extracted correctly for subject' + str(subject_num) + '_' + label + measurement)
						continue # skip data if not succesfully extracted

		# Normalize and standarize data
					normalize_and_standarize.standarize(Exp_data)

		# Rotate data (apply PCA transformation)
					PCA_Transform.PCA_Transform(Exp_data, 3)

		# Extract samples
					Sampled_data = Sample(Exp_data)
					Sampled_data.segment_into_samples(Exp_data)

					if Sampled_data.number_of_data_points_in_one_step < minP:
						minP =  Sampled_data.number_of_data_points_in_one_step # get minimum frame number

		# Accumulate sampled data into single array
					list_of_samples.append(Sampled_data) # every element of the list is a Sample object.

		# Plot data
					#plot_data.plot_experiment_data(Exp_data)
					#plot_data.plot_sampled_data(Sampled_data)

				except:
					continue

	# Resample all data to lowest frame number
	resampled_list = resample_all_data.resample_data(list_of_samples, minP) # every element of the list is a Sample object.

	# Plot resmapled data
	#plot_data.plot_resampled_data(resampled_list)

	# Arrange data in single multidimensional numpy array to feed ANN and create corresponding array with labels.
	# The two arrays returned can be feeded to the ANN.
	return arrange_data_for_ann.arrange_data(resampled_list)

