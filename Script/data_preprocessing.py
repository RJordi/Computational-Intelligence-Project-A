import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.decomposition import PCA


path = os.getcwd()

subject = np.arange(150, 174, 1).tolist()
rep = ["01","02"]

for i in subject:
    for j in rep:
        try:
            df = pd.read_csv(path + "\\subject"+str(i)+"_downstairs"+j+"\Accelerometer.csv")
            df = df.drop( columns = df.columns[0])
        except: 
            pass
            
