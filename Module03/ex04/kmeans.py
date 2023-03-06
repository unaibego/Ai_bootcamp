import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename =filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("something bad has occurred")
        return True

    def getdata(self):
        self.f = open(self.filename, "r")
        if self.header:
            out = self.f.read()
        else :
            out = self.f.readline()
            out = self.f.read()
        return(out.split(self.sep))
    def getheader(self):
        self.f = open(self.filename, "r")
        if self.header:
            out = self.f.readline()
            return(out.split(self.sep))
        else :
            return None
class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids
    def fit(self, X):
        clustered_data = []
        random_centroid_index = random.sample(range(len(X)), self.ncentroid)
        for i in range(self.ncentroid):
            clustered_data.append([])
        random_centroid = []
        for i in range(self.ncentroid):
            random_centroid.append(X[random_centroid_index[i]])
        for h in range(self.max_iter):
            for i in range(self.ncentroid):
                clustered_data[i] = []
            for j in range(len(X)):
                min_distance = 100000
                for i in range(len(random_centroid_index)):
                    new_distance = distance(X[j], random_centroid[i])
                    if new_distance < min_distance:
                        min_distance = new_distance
                        index = i
                clustered_data[index].append(X[j])
            for i in range(self.ncentroid):
                random_centroid[i][0] = np.array(clustered_data[i])[:,0].mean()
                random_centroid[i][1] = np.array(clustered_data[i])[:,1].mean()
                random_centroid[i][2] = np.array(clustered_data[i])[:,2].mean()
        self.centroids = random_centroid
        self.plot_points(clustered_data)
        
    def predict(self, X):
        pass
    def plot_points(self, clustered_data):
        fig = plt.figure(figsize=(4,4))
        ax = fig.add_subplot(111, projection='3d')
        colors = ["red", "green", "blue", "orange", "grey", "black", "white"]
        for j in range(self.ncentroid):
            for i in clustered_data[j]:
                ax.scatter(i[0],i[1],i[2], color = colors[j])
        plt.show()



def distance(p1, p2):
    return ((((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2)+((p1[2]-p2[2])**2))**0.5)

# X = [[random.randint(0,10),random.randint(0,10),random.randint(0,10)] for i in range(30)]
# Kmean = KmeansClustering()
# Kmean.fit(X)

if __name__ == "__main__":
    with CsvReader(sys.argv[1]) as file:
        data = file.getdata()
        new_data = data[0].split("\n")
        print(new_data)
        header = file.getheader()
