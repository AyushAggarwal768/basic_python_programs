#Q.3 - Create a numpy array A of shape(10,20) and B of shape (20,25) using np.random.
#Print the matrix which is the matrix multiplication of A and B.
#The shape of the new matrix should be (10,25). Using basic numpy math functions only find the sum of all the elements of the new matrix.

import numpy as np

a = np.random.rand(10,20)
b = np.random.rand(20,25)
c = (np.dot(a,b))
print(c)
print("Shape ->",c.shape)
print("Sum ->",np.sum(c))
