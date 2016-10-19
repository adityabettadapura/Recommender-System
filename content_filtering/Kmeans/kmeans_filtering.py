import csv
import numpy as np
from scipy.cluster.vq import kmeans2
from collections import defaultdict

def KmeansFiltering(inputfile, outputfile):
    """
    :param inputfile: Feature vector for each movie
    :param outputfile: Kmeans classification of each movie
    :return: Recommendation of similar movies
    """

    # Read in genre vector from file
    infile = open(inputfile, 'rb')
    filereader = csv.reader(infile)
    genreVector = next(filereader)

    for row in filereader:
        genreVector = np.vstack([genreVector, row])
    
    # Perform kmeans clustering
    centroids, labels = kmeans2(genreVector, 18)
    new = list(labels)
    
    outfile = open(outputfile, 'wb')
    filewriter = csv.writer(outfile)
    filewriter.writerows(new)

    # Generate recommendations based on movies in same cluster
    i=0
    recommendation = defaultdict(list)
    infile = open('kmeans.txt', 'rb')
    lines = infile.read().splitlines()
    lines = lines[1:]
    for row in lines:
        recommendation[row].append(i)
        i = i+1

    return recommendation
