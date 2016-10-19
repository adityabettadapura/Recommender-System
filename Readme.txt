Readme.txt
----------

This is a python based recommender system for movies. This consists of two different recommender systems. Content based recommender systems which use kmeans and pairwise distances to recommend movies. The collaborative filtering model uses learning techniques and conjugate gradient to train the system to recommend movies as per user ratings. The data set used for this project has been obtained from http://grouplens.org/datasets/movielens/. The data set consists of 10329 movies and has ratings provided by 668 users. 


License information
-------------------
Dataset citation:
F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4, Article 19 (December 2015), 19 pages. DOI=http://dx.doi.org/10.1145/2827872

Further details and usage license can be found in ml-latest-small-README.html


List of Files
-------------
1. Content based filtering (Kmeans):
	1. main.py - Entry point of main. Calls feature extraction and kmeans subroutines. Displays top ten recommendations.
	2. featextract.py - Creates feature vector for each movie based on the genres it is tagged with.
	3. kmeans_filtering.py - Performs kmeans clustering to classify the movies
	4. kmeans.png - Screenshot of the output.

2. Content based filtering (Pairwise distance):
	1. main.py - Calls feature extraction, and pdist subroutines. Displays top ten recommendations based on similarity.
	2. featextract.py - Creates feature vector for each movie based on the genres it is tagged with.
	3. pairdistances.py - Computes the pairwise distance between each pair of movies. 
	4. toppdistresult.py - Obtains top ten closest movies to each movie in the data set.
	5. pdist.png - Screenshot of the output.

3. Collaborative filtering:
	1. main.py - Processes the data set to obtain input matrices and allows the user to rate a movie, and gets top ten recommendations based on user preferences.
	2. processDataCollabFilter.py - Process the data set and returns movies-user ratings matrices.
	3. collaborativeFiltering.py - Trains random weights and predicts movie preferences for the user based on cost minimization using conjugate gradient method.
	4. generateWeights.py - Generates random initial weights.
	6. costFunction.py - Computes cost, which is a function of the training weights and input movie-user rating matrices/
	5. computeGradients.py - Computes the gradients (first order derivatives) of the given training weights.
	7. normalization.py - Mean normalizes a given matrix. Uses the formula: A_mean = (A - mean(A))/std.dev(A)
	8. collaborative.png - Screenshot of the output.
	

To run the programs
-------------------
1. Download the data set from http://grouplens.org/datasets/movielens/ and place the .csv files in the same folder as the source files.
2. Run main() for each system to obtain respective results.

