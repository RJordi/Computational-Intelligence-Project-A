#CIE Project A
#Notes:

print("Loading function files\n")
from read_csv import Data
from plot_data import plot_data
from extract_motion_sequence import extract_sequence
print("Function files complete\n")

print("Loading Libraries\n")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from scipy.signal import find_peaks
from scipy import signal
print("Libraries Loaded\n")

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

class Sample:
    def __init__(self,experiment):
        self.samples = [[[]]] #here comes the fun part with high dimsneional matrices - quick diagram to explain:
        # samples[i][j][k]
        # i = experiment#, ie i=1 is normal 01
        # j = step#
        # k = x,y,z - 0 : x, 1 : y, 2 : z
        for i in range(2):
            peaks, _ = find_peaks(experiment.experimentList[i].x,height=1.5,distance = 150) #peaks is the index of the data
            sumPeaks = 0
            for j in range(len(peaks)-1):
                sumPeaks = sumPeaks + peaks[j+1]-peaks[j]
            
            average = sumPeaks/(len(peaks)-1)
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
            
            for j in range(len(index)):
                indexLower = index[j][0]
                indexUpper = index[j][1]
                print(indexUpper)
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
        experiment.experimentList[i].time = experiment.experimentList[i].time.dropna().to_numpy() #turned into numpy
        experiment.experimentList[i].sampleNo = np.linspace(0,len(experiment.experimentList[i].x-1),len(experiment.experimentList[i].x))


subject = 238
experiment1 = experiment(subject)
#Extract motion sequence from all experiments and walking positions
#plt.plot(experiment1.normal(2).sampleNo,experiment1.normal(2).x)
for i in range(8):
    extract_sequence(experiment1.experimentList[i]) #please include sample# in the extract_csv function

for i in range(8):
    experiment1.experimentList[i].sampleNo = np.linspace(0,len(experiment1.experimentList[i].x)-1,len(experiment1.experimentList[i].x))
    

#plt.plot(experiment1.normal(2).sampleNo,experiment1.normal(2).x)
PCA_Transform(experiment1,3)
#plt.plot(experiment1.normal(2).sampleNo,experiment1.normal(2).x)

#plt.legend(['pre-PCA,pre Extraction','pre-PCA, post extraction','post-PCA and extraction'])
fig3 = plt.figure()
peaks, _ = find_peaks(experiment1.experimentList[1].x,height=1.5,distance = 150) #peaks is the index of the data
plt.plot(experiment1.experimentList[1].x)
plt.plot(peaks,experiment1.experimentList[1].x[peaks],"x")
#plt.show()

sumPeaks = 0
fig1 = plt.figure()
for i in range(len(peaks)-2):
    plt.plot(experiment1.experimentList[1].x[peaks[i]:peaks[i+1]])
for i in range(len(peaks)-1):
    sumPeaks = sumPeaks + peaks[i+1]-peaks[i]

average = sumPeaks/(len(peaks)-1)
count = 0;
fig2 = plt.figure()
#Pre resampling plot - can keep somewhere to test future experiments
for i in range(len(peaks)-1):
    if (peaks[i+1]-peaks[i] >= 1.3*average or peaks[i+1]-peaks[i] <= 0.8*average):
        continue
    else:
        plt.plot(experiment1.experimentList[1].x[peaks[i]:peaks[i+1]])
        count = count + 1
#post resampling
sample1 = Sample(experiment1)
fig4 = plt.figure()
for i in range(len(sample1.samples[0])-1):
    print(i)
    plt.plot(sample1.samples[1][i][0])
