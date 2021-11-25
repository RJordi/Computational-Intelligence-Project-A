##############################
### Preprocess data
### main file
##############################

from read_csv import Data
import filter_data
import plot_data
import extract_motion_sequence
import normalize_and_standarize

# Read csv data
for subject_num in range(236, 237):
	for label in ['downstairs', 'normal', 'upstairs']:
		for measurement in ['01', '02']:
			try:
				Exp_data = Data(subject_num, label, measurement)
				Exp_data.extract_csv()
				#print(Exp_data.time, Exp_data.x, Exp_data.y, Exp_data.z)
				#print('Frequency for subject' + str(subject_num) + '_' + label + measurement + ' is: ' + str(Exp_data.frequency))
			except:
				print('Data for subject'+ str(subject_num) + '_' + label + measurement + ' is not available.')
				continue
				# another option would be to put the try except clauses in the class function extract_csv()
				# and when entering the except case we create a boolean attribute called self.available with False value

# Filter data
			#filter_data.filter_data(Exp_data)

# Extract frequency
			#extract_motion_sequence.extract_sequence(Exp_data)

# Normalize and standarize data
			#normalize_and_standarize.normalize(Exp_data)
			#normalize_and_standarize.standarize(Exp_data)

# Plot data
			plot_data.plot_data(Exp_data)

