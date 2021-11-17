# Normalizing data uzing Tanh formula # 

def normalize(experiment):
    m = experiment.x.mean()
    std = experiment.x.std()
    df_mod = 0.5 * (np.tanh(0.01 * ((experiment.x - m) / std)) + 1)
    experiment.x  = df_mod

    m = experiment.y.mean()
    std = experiment.y.std()
    df_mod = 0.5 * (np.tanh(0.01 * ((experiment.y - m) / std)) + 1)
    experiment.y  = df_mod

    m = experiment.z.mean()
    std = experiment.z.std()
    df_mod = 0.5 * (np.tanh(0.01 * ((experiment.z - m) / std)) + 1)
    experiment.z  = df_mod
    
