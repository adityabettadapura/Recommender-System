import numpy as np
from scipy import optimize
from generateWeights import GetWeights
from costFunction import CostFunc
from computeGradients import ComputeGrad
from normalization import MeanNormalize


def GetRecommendation(Y, R, num_movies, num_users, num_features):

    # Initialize weights to random values
    X, Theta = GetWeights(num_movies, num_users, num_features)

    # Minimize cost function using updated values of X and Theta
    # Result will contain final trained values for X and Theta
    x0 = np.append(X.flatten(), Theta.flatten())
    result = optimize.fmin_cg(CostFunc, x0, fprime=ComputeGrad, args=(Y, R), maxiter=5)

    # Reshape X and Theta to original dimensions
    X_final = np.reshape(result[0:num_movies * num_features], (num_movies, num_features))
    Theta_final = np.reshape(result[num_movies * num_features:], (num_users, num_features))

    # Mean normalization of Movie-Ratings matrix
    Y_mean = MeanNormalize(Y)

    # Get predicted values
    prediction = np.dot(X_final, Theta_final.T) + Y_mean

    return prediction
