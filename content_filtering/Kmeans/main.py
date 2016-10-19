from kmeans_filtering import KmeansFiltering

def main():
    # The different genres obtained from the data set
    genrelist = ['Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
          'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western',
          '(no genres listed)']
    
    # Form feature 1x18 feature vectors for each movie
    ExtractFeatures(genrelist, 'movies.csv', 'out.csv')
    
    # Perform kmeans clustering to see matches for each movie
    recommendation = KmeansFiltering('out.csv', 'kmeans.csv')

    # Suggest top ten matches for each movie as per user choice
    lines = open('movies.csv').readlines()
    for i in range(1,11,1):
        print i, lines[i].split(",")[1]

    user = input("Choose a movie (1-10): ")
    topten = recommendation[str(user)][0:10]
    print "Top ten suggestions for you:"
    for item in topten:
        print lines[item].split(",")[1]


if __name__ == "__main__":
    main()