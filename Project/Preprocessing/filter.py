from scipy.signal import savgol_filter

def filter(experiment)
    experiment.x = savgol_filter(experiment.x, 70, 3)
    experiment.y = savgol_filter(experiment.y, 70, 3)
    experiment.z = savgol_filter(experiment.z, 70, 3)
