import csv
import numpy as np


def ExtractFeatures(genres, inputfile, outputfile):
    """
    :param genres: List of genres/classes in the product
    :param inputfile: Input file of movies with their genre tags
    :param outputfile: Feature vector for each movie
    :return: void
    """
    
    # Form genre vector
    i = 0
    genreValue = dict()
    for genre in genres:
        genreValue[genre] = i
        i += 1

    # for each movie create its genre vector
    genreVector = np.zeros(len(genres))
    infile = open(inputfile, 'rb')
    filereader = csv.reader(infile)
    next(filereader)

    for row in filereader:
        moviegenre = row[2].split("|")
        tempvec = np.zeros(len(genres))
        for item in moviegenre:
            if item in genreValue:
                tempvec[genreValue[item]] = 1

        genreVector = np.vstack([genreVector, tempvec])

    # create a file with genreVectors
    outfile = open(outputfile, 'wb')
    filewriter = csv.writer(outfile)
    filewriter.writerows(genreVector[1:])

