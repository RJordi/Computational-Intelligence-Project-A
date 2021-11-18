from scipy.signal import savgol_filter

def filter_data(experiment):
    experiment.x = savgol_filter(experiment.x, 71, 3)
    experiment.y = savgol_filter(experiment.y, 71, 3)
    experiment.z = savgol_filter(experiment.z, 71, 3)
