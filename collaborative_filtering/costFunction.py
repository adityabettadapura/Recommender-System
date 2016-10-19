import numpy as np


def CostFunc(x0, *args):
    """
    Cost function is a multivariate function in X and Theta
    :param x0: Consists of X and Theta rolled into a single array
    :param args: Movies-Ratings matrices Y and R
    :return: Cost (scalar value)
    """

    # Passed as args
    Y, R = args

    # Unroll X and Theta from x0
    num_feat = x0.shape[0]/(Y.shape[0]+Y.shape[1])
    num_movies = Y.shape[0]
    num_users = Y.shape[1]

    X = np.reshape(x0[0:num_movies * num_feat], (num_movies,num_feat))
    Theta = np.reshape(x0[num_movies * num_feat:], (num_users,num_feat))
    theta_t = np.transpose(Theta)

    # Calculate cost
    J = np.sum(np.square(np.dot(X, theta_t)*R - Y*R))

    return J
