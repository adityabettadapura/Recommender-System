import csv
import numpy as np
from scipy.spatial.distance import pdist, squareform

def GetPairwiseDistances(inputfile, outputfile):
    """
    :param inputFile: File containing feature vector for each product
    :param outputFile: File containing pairwise distances between all products
    :return: void
    """
    
    # Read genrevector from file
    infile = open(inputfile, 'rb')
    filereader = csv.reader(infile)
    genreVector = next(filereader)

    for row in filereader:
        genreVector = np.vstack([genreVector, row])

    # Compute pairwise distances for each movie
    Y = pdist(genreVector, 'euclidean')
    X = squareform(Y)

    # Write out result to file
    outfile = open(outputfile, 'wb')
    filewriter = csv.writer(outfile)
    filewriter.writerows(X)
