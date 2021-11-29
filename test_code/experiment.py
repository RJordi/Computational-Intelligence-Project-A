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

class experiment:
    def __init__(self,subject):
        self.walkingForm = ['normal','upstairs','downstairs','impaired']
        self.experimentNo = ['01','02']
        self.experimentList = []
        it=0
        for i in self.walkingForm:
            for j in self.experimentNo:
                self.experimentList.append(Data(subject,i,j))
                self.experimentList[it].extract_csv()
                self.experimentList[it].sampleNo = np.linspace(0,len(self.experimentList[it].x)-1,len(self.experimentList[it].x))
                it = it+1
        
    def normal(self,str1):
        if str(str1) == '01' or str(str1) == '1':
            return self.experimentList[0]
        elif str(str1) == '02' or str(str1) == '2':
            return self.experimentList[1]
        
    def upstairs(self,str1):
        if str(str1) == '01' or str(str1) == '1':
            return self.experimentList[2]
        elif str(str1) == '02' or str(str1) == '2':
            return self.experimentList[3]
    
    def downstairs(self,str1):
        if str(str1) == '01' or str(str1) == '1':
            return self.experimentList[4]
        elif str(str1) == '02' or str(str1) == '2':
            return self.experimentList[5]
    
    def impaired(self,str1):
        if str(str1) == '01' or str(str1) == '1':
            return self.experimentList[6]
        elif str(str1) == '02' or str(str1) == '2':
            return self.experimentList[7]