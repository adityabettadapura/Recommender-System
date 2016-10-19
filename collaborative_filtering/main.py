from collaborativeFiltering import GetRecommendation
from processDataCollabFilter import ProcessInput
import heapq


def main():

    # Constants based on input dataset
    num_movies = 10329
    num_users = 668
    num_features = 10

    # Process input to get Movie-Ratings matrices
    Y, R = ProcessInput('movies.csv', 'ratings.csv', num_movies, num_users)

    # Get user rating
    user = input("Enter user number (1-668): ")
    movie = input("Choose a movie to rate (1-10329): ")
    rating = input("Give rating (1-5): ")

    # Change rating in movie ratings matrix
    Y[movie-1][user-1] = rating
    R[movie-1][user-1] = 1

    # Get recommendations based on user preference
    Recommendation = GetRecommendation(Y, R, num_movies, num_users, num_features)

    # Select top ten recommended movies
    topten = heapq.nlargest(10, enumerate(Recommendation[:, user-1]), key=lambda x: x[1])

    # Display top suggestions for the user
    lines = open('movies.csv').readlines()
    result = [lines[i[0] + 1].split(',')[1] for i in topten]
    print "Top recommendations for user",user,":"
    for item in result:
        print item


if __name__ == "__main__":
    main()
