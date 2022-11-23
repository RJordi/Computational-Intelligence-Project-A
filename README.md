# Neural network for path classification

This project consists of a feedforward neural network that predicts if a person is walking upstairs, downstairs or on a flat surface. It was developed as part of the Computational Intelligence course at [RWTH Aachen University] (https://www.rwth-aachen.de). 


Overview
-------
The data was obtained from experiments performed by the students participating in the course. In these experiments, students recorded the accelerometer and gyroscope data of their phones with [phyphox] (https://phyphox.org/) while walking upstairs, downstairs and on a flat surface. The phone was placed in the right back pocket during the experiments.
For this neural network, only the accelerometer data is used. The accelerometer data is given at a certain frequency for each space coordinate (x,y,z). 

The data processing steps are summarized in the figure below:
![Data Processing Diagram](https://github.com/RJordi/walking-path-detection/blob/master/data_processing_diagram.png)


Code structure
-------
The project is structured as follows:
- `code/`
	- `preprocessing/`: Data preprocessing functions.
		- `read_csv.py`: Read data and create base object class. 
		- `filter_data.py`: Filter accelerometer signal with Savitzky–Golay filter.
		- `extract_motion_sequence.py`: Extract relevant information from each data instance.
		- `normalize_and_standardize.py`: Normalize and standardize data.
		- `PCA_Transform.py`: Apply PCA transformation to acceleration vector components.
		- `segment_into_samples.py`: Sample acceleration signal based on the signal peaks.
		- `resample_all_data.py`: Resample all data points to the lowest frame number.
		- `arrange_data_for_ann.py`: Arrange data into a single multidimensional numpy array.
		- `plot_data.py`: Plotting functions.
	- `ann/`: .
		-`main_ann.py`: Main function to run the neural network.
		-`run_ann.py`: Create feedforward neural network and run it using 10-fold cross-validation.
	- `main.py`: Main function to run the code.
