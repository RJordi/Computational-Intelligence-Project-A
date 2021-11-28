from sklearn.decomposition import PCA
import numpy as np

def PCA_Transform(experiment,components):

	acc_vector = np.vstack((experiment.x, experiment.y, experiment.z)).T

	pca = PCA(n_components = components)
	pca.fit(acc_vector)
	x_pca = pca.transform(acc_vector)

	#Storing the information once more into the experiment object
	experiment.x = x_pca[:,0]
	experiment.y = x_pca[:,1]
	experiment.z = x_pca[:,2]
	experiment.sampleNo = np.linspace(0,len(experiment.x-1),len(experiment.x))

	#print(experiment.sampleNo)