from experiment import experiment
from PCA_Transform import PCA_Transform
from sample import Sample
from subjectResample import subjectResample
import matplotlib.pyplot as plt
import normalize_and_standarize

subject = 235

experiment1 = experiment(subject)
PCA_Transform(experiment1,3)
sample1 = Sample(experiment1)
subjectResample(sample1) #If this fails check to see if the sample object had
#a fatal error. That's typically the reason for this function to not work


#can look at how the resampled stuff looks like
normalWalk = sample1.samples[0]
plt.figure()
for i in range(len(normalWalk)-1):
    plt.plot(normalWalk[i][1])
plt.figure()  
for i in range(len(normalWalk)-1):
    plt.plot(normalWalk[i][0])
