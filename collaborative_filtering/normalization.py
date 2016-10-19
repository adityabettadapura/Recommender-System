import numpy as np

def MeanNormalize(Y):
    """
    :param Y: Movies-user ratings matrix
    :return: Y, mean normalized
    """
    return (Y - np.mean(Y, axis=0))/np.std(Y, axis=0)