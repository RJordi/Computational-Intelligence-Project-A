from scipy import signal

def subjectResample(sample):
        minP = 10000
        for i in range(8):
            if len(sample.samples[i][0][0]) < minP:
                minP = len(sample.samples[i][0][0])
        
        for i in range(8):
            for j in range(len(sample.samples[i])-1):
                sample.samples[i][j][0] = signal.resample(sample.samples[i][j][0],minP)
                sample.samples[i][j][1] = signal.resample(sample.samples[i][j][1],minP)
                sample.samples[i][j][2] = signal.resample(sample.samples[i][j][2],minP)

