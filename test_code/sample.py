from read_csv import Data
from plot_data import plot_data
from extract_motion_sequence import extract_sequence
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from scipy.signal import find_peaks
from scipy import signal
#Note sure which libraries to delete for now xD

class Sample:
    def __init__(self,experiment):
        self.samples = [[[]]] #here comes the fun part with high dimsneional matrices - quick diagram to explain:
        # samples[i][j][k]
        # i = experiment#, ie i=1 is normal 01
        # j = step#
        # k = x,y,z - 0 : x, 1 : y, 2 : z
        for i in range(len(experiment.experimentList)):
            peaks, _ = find_peaks(experiment.experimentList[i].x,height=1.5,distance = 150) #peaks is the index of the data
            sumPeaks = 0
            division = 1
            for j in range(len(peaks)-1):
                if peaks[j+1]-peaks[j] > 4* (peaks[j]-peaks[j-1]):
                    if j == 2 or 1:
                        print("Outlier peak for i = "+str(i) + " Observe data")
                        division = division + 1
                        continue
                    elif peaks[j+1]-peaks[j] > 4* (peaks[j-1]-peaks[j-2]):
                        print("Outlier peak for i = "+str(i) + " Observe data")
                        division = division + 1
                        continue
                    else:
                        print("Outlier Ignored for i = "+str(i))
                        continue
                else:
                    sumPeaks = sumPeaks + peaks[j+1]-peaks[j]
                
            
            average = sumPeaks/(len(peaks)-division)
            #Next we find the useable ranges and put them into a list... very convoluted but open for ideas xD
            index = []
            minP = 1000 #this will be used to find the minimum amount of data points
            for j in range(len(peaks)-1):
                if (peaks[j+1]-peaks[j] >= 1.3*average or peaks[j+1]-peaks[j] <= 0.8*average):
                    continue
                else:
                    index.append([peaks[j],peaks[j+1]])
                    if (peaks[j+1] - peaks[j] < minP):
                        minP = peaks[j+1] - peaks[j] #minimum amount of data points found here, we resample everything to this value
            
            if len(index) == 0:
                print("There are no peaks for i = " + str(i))
                break
            
            for j in range(len(index)):
                indexLower = index[j][0]
                indexUpper = index[j][1]
                orDatax = experiment.experimentList[i].x[indexLower:indexUpper]
                orDatay = experiment.experimentList[i].y[indexLower:indexUpper]
                orDataz = experiment.experimentList[i].z[indexLower:indexUpper]
                tempArrayx = signal.resample(orDatax,minP)
                tempArrayy = signal.resample(orDatay,minP)
                tempArrayz = signal.resample(orDataz,minP)
                self.samples[i][j].append(tempArrayx)
                self.samples[i][j].append(tempArrayy)
                self.samples[i][j].append(tempArrayz)
                #i : experiment #
                #j : step #
                self.samples[i].append([]) #create new space for next sample   
            self.samples.append([[]]) # create new space for next experiment
            
            #print("For i = "+ str(i))
            #print(index)
            #print("With an index length of = " + str(len(index)))
            #print("With a minimum value of : "+ str(minP))