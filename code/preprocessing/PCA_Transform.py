from read_csv import Data
from extract_motion_sequence import extract_sequence
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from scipy.signal import find_peaks
from scipy import signal

def PCA_Transform(experiment,components):
    numCases = 8
    for i in range(numCases):
        #Data Frame Transformations
        #print("Case =" + str(i))
#        df1 = experiment1.experimentList[i].x.to_frame()
#        df2 = experiment1.experimentList[i].y.to_frame()
#        df3 = experiment1.experimentList[i].z.to_frame()
#        dfMatrix = pd.concat([df1,df2,df3], axis=1)
#        dfMatrix = dfMatrix.dropna() 
#       inquire about NaN
        #the above are just in case we go back to using pandas dataframe
        
        #removing NaNs. Don't understand, don't care - it works
        experiment.experimentList[i].x = experiment.experimentList[i].x[~np.isnan(experiment.experimentList[i].x)]
        experiment.experimentList[i].y = experiment.experimentList[i].y[~np.isnan(experiment.experimentList[i].y)]
        experiment.experimentList[i].z = experiment.experimentList[i].z[~np.isnan(experiment.experimentList[i].z)]
        experiment.experimentList[i].time = experiment.experimentList[i].time[~np.isnan(experiment.experimentList[i].time)]
        #Creating 2d matrix
        dfMatrix = np.vstack((experiment.experimentList[i].x, experiment.experimentList[i].y, experiment.experimentList[i].z)).T
        #PCA Process
        pca = PCA(n_components = components)
        pca.fit(dfMatrix)
        x_pca = pca.transform(dfMatrix)
        #Storing the information once more into the experiment object
        experiment.experimentList[i].x = x_pca[:,0]
        experiment.experimentList[i].y = x_pca[:,1]
        experiment.experimentList[i].z = x_pca[:,2]