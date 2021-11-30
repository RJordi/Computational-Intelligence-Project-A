import sys
import numpy as np
sys.path.append('./preprocessing')
sys.path.append('./ann')

import main_preprocess
import main_ann

print('-------- PROGRAM STARTED --------')

samples_tensor, labels_array, subjects_array = main_preprocess.main_preprocess()

#print('Shape of samples tensor:', np.shape(samples_tensor))
#print('Shape of labels array:', np.shape(labels_array))

main_ann.main_ann(samples_tensor, labels_array, subjects_array)