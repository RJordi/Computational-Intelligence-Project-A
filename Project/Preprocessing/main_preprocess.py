##############################
### Preprocess data
### main file
##############################

from read_csv import Data

# Read csv data
for subject_num in range(150, 275):
	for label in ['downstairs', 'normal', 'upstairs']:
		for measurement in ['01', '02']:
			try:
				Exp_data = Data(subject_num, label, measurement)
				Exp_data.extract_csv()
				#print(Exp_data.time, Exp_data.a_x, Exp_data.a_y, Exp_data.a_z)
				#print('Frequency for subject' + str(subject_num) + '_' + label + measurement + ' is: ' + str(Exp_data.frequency))
			except:
				print('Data for subject'+ str(subject_num) + '_' + label + measurement + ' is not available.')
				# another option would be to put the try except clauses in the class function extract_csv()
				# and when entering the except case we create a boolean attribute called self.available with False value

# Extract frequency