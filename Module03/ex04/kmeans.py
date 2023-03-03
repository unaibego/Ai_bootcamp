import random

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids
    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        None.
        Raises:
        -------
        This function should not raise any Exception.
        """
        clustered_data = []
        for i in range(self.ncentroid):
            clustered_data.append([])
        random_centroid_index = random.sample(range(len(X)), self.ncentroid)
        for j in range(len(X)):
            min_distance = 100000
            for i in range(len(random_centroid_index)):
                new_distance = distance(X[j], X[random_centroid_index[i]])
                if new_distance < min_distance:
                    min_distance = new_distance
                    index = i
            clustered_data[index].append(X[j])
        for i in range(len(clustered_data)):
            print(clustered_data[i])
        pass
    def predict(self, X):  
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
        This function should not raise any Exception.
        """
        pass
def distance(p1, p2):
    return ((((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2)+((p1[2]-p2[2])**2))**0.5)

X = [[random.randint(0,10),random.randint(0,20),random.randint(0,30)] for i in range(100)]
Kmean = KmeansClustering()
Kmean.fit(X)