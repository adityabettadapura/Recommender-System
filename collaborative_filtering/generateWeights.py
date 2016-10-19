import numpy as np

def GetWeights(num_movies, num_users, num_features):
    """
    :param num_movies: Global constant. Total number of movies in the data set .
    :param num_users: Global constant. Total number of users in the data set.
    :param num_features: Total number of features chosen to train X and Theta.
                         More features leads to better fine tuning.
    :return: Randomly initialized values for X and Theta
    """

    # Initialize X and Theta to random values
    X = np.random.rand(num_movies, num_features)
    theta = np.random.rand(num_users, num_features)

    return X, theta
