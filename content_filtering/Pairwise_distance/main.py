from featextract import ExtractFeatures
from pairdistances import GetPairwiseDistances
from toppdistresult import CreateTopTenMatches

def main():
    # The different genres obtained from the data set
    genrelist = ['Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
          'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western',
          '(no genres listed)']

    # Form feature 1x18 feature vectors for each movie
    ExtractFeatures(genrelist, 'movies.csv', 'out.csv') 
    
    # Get pairwise distance between each movie
    GetPairwiseDistances('out.csv', 'pdist.csv')

    # Create a list of top ten matches for each movie 
    CreateTopTenMatches('pdist.csv', 'topten.csv')
    
    # Suggest top ten matches for each movie as per user choice
    lines = open('movies.csv').readlines()
    for i in range(1,11,1):
        print i, lines[i].split(",")[1]

    topten = open('topten.csv', 'rb').readlines()
    user = input("Choose a movie (1-10): ")
    movies = topten[user].rstrip('\r\n').split(",")
    print "Top ten suggestions for you:"
    for item in movies:
        print lines[int(item)].split(",")[1]


if __name__ == "__main__":
    main()