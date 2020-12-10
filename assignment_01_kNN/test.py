import numpy as np
from k_nearest_neighbour import KNearestNeighbor
from scipy.spatial import distance

X_test = np.random.rand(2, 5)
X_train = np.random.rand(3, 5)
print("X_test: ", X_test)
print("X_train: ", X_train)
num_test = X_test.shape[0]
num_train = X_train.shape[0]
