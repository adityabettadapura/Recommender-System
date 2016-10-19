import numpy as np

def ComputeGrad(x0, *args):
    """
    Computes gradient (first order derivatives) of X and Theta.
    :param x0: Consists of X and Theta rolled into a single array
    :param args: Movies-Ratings matrices Y and R
    :return: Returns gradients of X and Theta rolled into a single array
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

    # Compute gradient of X and Theta
    X_grad = np.dot((np.dot(X, theta_t)*R - Y*R), Theta)
    Theta_grad = np.dot(np.transpose(np.dot(X, theta_t) * R - Y * R), X)

    # Roll X and Theta gradients into a single array and return
    grad = np.append(X_grad.flatten(), Theta_grad.flatten())
    return grad