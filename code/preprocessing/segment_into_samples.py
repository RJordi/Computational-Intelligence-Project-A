from scipy import signal
import numpy as np

class Sample:
    def __init__(self, experiment):
        self.x = []
        self.y = []
        self.z = []
        self.title = experiment.subject_number + '_' + experiment.label + '_' + experiment.measurement
        self.label = experiment.label

    def segment_into_samples(self, experiment):
        flag = 0
        peaks, _ = signal.find_peaks(experiment.x,height=1.5,distance = 150) #peaks is the index of the data
        #print(peaks)
        sumPeaks = 0
        division = 1
        for j in range(len(peaks)-1):
            if peaks[j+1]-peaks[j] > 3* (peaks[j]-peaks[j-1]):
                if j == 2 or 1:
                    #print('Outlier peak for subject' + str(experiment.subject_number) + '_' + experiment.label + experiment.measurement)
                    division = division + 1
                    continue
                elif peaks[j+1]-peaks[j] > 3* (peaks[j-1]-peaks[j-2]):
                    #print('Outlier peak for subject' + str(experiment.subject_number) + '_' + experiment.label + experiment.measurement)
                    division = division + 1
                    continue
                else:
                    #print('Outlier Ignored for subject' + str(experiment.subject_number) + '_' + experiment.label + experiment.measurement)
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
            print("sample function: Fatal Error: \nThere are no peaks for i = " + str(i)+"\nExiting Program")
            flag = 1
            return
        
        for j in range(len(index)):
            indexLower = index[j][0]
            indexUpper = index[j][1]
            orDatax = experiment.x[indexLower:indexUpper]
            orDatay = experiment.y[indexLower:indexUpper]
            orDataz = experiment.z[indexLower:indexUpper]
            tempArrayx = signal.resample(orDatax,minP)
            tempArrayy = signal.resample(orDatay,minP)
            tempArrayz = signal.resample(orDataz,minP)
            self.x.append(tempArrayx)
            self.y.append(tempArrayy)
            self.z.append(tempArrayz)
        #print(np.shape(self.x))
        #print(np.shape(self.y))
        #print(np.shape(self.z))
        self.number_of_steps = np.shape(self.x)[0]
        self.number_of_data_points_in_one_step = np.shape(self.x)[1]
        #print('Number of steps:', self.number_of_steps)
        #print('Number of data points per step:',self.number_of_data_points_in_one_step)

        if flag == 1:
            plt.figure()
            print("Plotting Problem Curve")
            for j in range(len(peaks)-1):
                plt.plot(experiment.experimentList[i].x[peaks[j]:peaks[j+1]])
            plt.show()
