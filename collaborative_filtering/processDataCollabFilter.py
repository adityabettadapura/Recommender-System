import csv
import numpy as np

def ProcessInput(input1, input2, num_movies, num_users):
    """
    :param input1: File containing movie names and ids
    :param input2: File containing movie ratings by users
    :param num_movies: Total number of movies in the data set
    :param num_users: Total number of users in the data set
    :return: Movie-User rating matrix (Y), Movie-User incidence matrix (R)
    """
    # Create Movies-User Ratings matrix
    moviefile = open(input1, 'rb')
    movies = csv.reader(moviefile)
    row = next(movies)

    Y = np.zeros((num_movies, num_users))
    movie_idx = dict()
    i = 0
    for row in movies:
        movie_idx[row[0]] = i
        i += 1


    # Create Movie-User ratings and incidence matrices. Movie i is 1 iff User j has rated it.
    ratingfile = open(input2, 'rb')
    ratings = csv.reader(ratingfile)
    row_rate = next(ratings)

    R = np.zeros((num_movies, num_users))

    for row_rate in ratings:
        r = movie_idx[row_rate[1]]
        c = int(row_rate[0])-1
        R[r, c] = 1
        Y[r, c] = float(row_rate[2])

    return Y, R

