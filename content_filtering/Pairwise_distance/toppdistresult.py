import csv
import heapq

def CreateTopTenMatches(inputFile, outputFile):
    """
    :param inputFile: File containing pairwise distances between all products
    :param outputFile: Writes Top N closest matches to each product
    :return: void
    """

    infile = open(inputFile, 'rb')
    outfile = open(outputFile, 'wb')

    filereader = csv.reader(infile)
    filewriter = csv.writer(outfile)

    # Obtain top ten result for each movie based on distance measure
    for row in filereader:
        distances = heapq.nsmallest(10, enumerate(row), key=lambda x: x[1])
        topten = [i[0] for i in distances]
        filewriter.writerow(topten)



