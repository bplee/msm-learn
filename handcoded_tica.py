# This is an attempt to hard code tICA in order to boost my understand of both the theory and practice of the method

import numpy as np
import matplotlib.pylab as plt
import mdtraj as md
from pyemma.coordinates import featurizer

# guy = '/Users/bren/downloads/run17clone3.h5'

# traj = md.load(guy)

# print ('data loaded')

# X = featurizer(traj.topology)

X = np.random.random([300,100])

# u = np.dot(np.mean(X.T, axis = 1).T, np.ones(np.shape(X)))

u = X.mean(axis=0)
 
print (u.shape)

print (u)

t = 20


# Alternatively calculating all the mean data first
meanless_x = X - u
meanless_x_0 = meanless_x[0:-t]
meanless_x_t = meanless_x[t:]

# Generating Covariance matrices
c_0 = np.dot((meanless_x_0).T, meanless_x_0)/(len(X)-t)
c_t = np.dot((meanless_x_t).T, meanless_x_t)/(len(X)-t)

c_0_inv = np.linalg.inv(c_0)

# Solving eigenstuff for tICA
eigvals, eigvects = np.linalg.eig(np.dot(c_0_inv,c_t))


def projection(dim = 2):
	basis = eigvects[:dim] # TODO, work on sorting the eigenvectors by largest eigenvalues
	X_new = np.zeros([len(X),dim])
	for i in range(len(X)):
		X_new[i] = np.dot(basis, X[i]).T
	return X_new

# print (projection())

#THIS IS AN EDIT SO THAT I CAN PRACTICE COMMITTING CHANGES AND PULLING THEM ON GITHUB
