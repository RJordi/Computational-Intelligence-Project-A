import tensorflow as tf
import numpy as np

import split_dataset
import run_ann

def main_ann(samples_tensor, labels_array):

	validation_tensor, validation_labels, test_tensor, test_labels, training_tensor, training_labels = split_dataset.split_dataset(samples_tensor, labels_array)

	run_ann.run_ann(validation_tensor, validation_labels, test_tensor, test_labels, training_tensor, training_labels)