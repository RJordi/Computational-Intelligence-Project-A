import sys
import numpy as np
sys.path.append('./preprocessing')

import main_preprocess

samples_tensor, labels_array = main_preprocess.main_preprocess()

print('Shape of samples tensor:', np.shape(samples_tensor))
print('Shape of labels array:', np.shape(labels_array))