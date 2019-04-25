Please read through Project description file.

# Method of implementation
Let the given platform be taken as a nxm matrix.
1. Take a nxm matrix of all 1's. This matrix, let's call it as drain_possibility matrix, holds the possibility of each position to hold water.
2. 1 implies water storage possible and 0 implies a drain.
3. Update all boundary elements of the drain_possibility matrix to 0's as they cannot hold water.
4. Traverse the original matrix leaving the boundaries.
5. For each position determine the posibility.
    1. If the value in that position is 0, it is already a drain and update the drain_possibility matrix at this position to 0.
    2. If the element is a peak, it cannot hold water, so marked as 0 in the drain_possibility matrix at that position.
    3. If there is a drain in one of its four neighbors (top, left, right, bottom), this position also cannot hold water. So 0.
    4. If one of its four neighbors is a possible drain and is in lower elevation to the current position, it also cannot hold        water, so 0. Otherwise it can hold water and is a 1.
6. The drain_possibility matrix is ready now. 
7. For calculating the quantity of the water stored, look for 1's in the drain_possibility matrix and its corresponding neighbors in the original matrix to calculate max units of water that position can hold.
8. Sum the water stored in all possible positions to obtain total water stored in the platform.

# Test cases
ex1 = np.array([[2, 2, 2], 
                [2, 2, 2], 
                [2, 2, 2]])

ex2 = np.array([[2, 2, 2, 2], 
                [2, 1, 2, 1], 
                [2, 2, 2, 1]])

ex3 = np.array([[3, 3, 3, 3, 3, 3], 
                [3, 1, 2, 3, 1, 3], 
                [3, 1, 2, 3, 1, 3], 
                [3, 3, 3, 1, 3, 3]])

ex4 = np.array([[3, 3, 3, 3, 5, 3], 
                [3, 0, 2, 3, 1, 3], 
                [3, 1, 2, 3, 1, 3], 
                [3, 3, 3, 1, 3, 3]])

ex5 = np.array([[5, 5, 5, 5, 5], 
                [9, 1, 1, 1, 5], 
                [5, 1, 5, 1, 5],
                [5, 1, 1, 1, 5],
                [5, 5, 5, 5, 5]])

ex6 = np.array([[5, 5, 5, 5, 5], 
                [9, 1, 0, 1, 5], 
                [5, 1, 5, 1, 5],
                [5, 1, 1, 1, 5],
                [5, 5, 5, 5, 5]])

ex7 = np.array([[5, 5, 5, 5, 5], 
                [9, 1, 0, 1, 5], 
                [5, 2, 5, 1, 5],
                [5, 1, 2, 1, 5],
                [5, 5, 5, 5, 5]])

ex8 = np.array([[2, 2, 2, 2], 
                [2, 1, 1, 1], 
                [2, 2, 2, 1],
                [2, 2, 2, 1]])

ex9 = np.array([[3, 3, 3, 3, 3, 3], 
                [3, 2, 2, 2, 1, 3], 
                [3, 2, 0, 2, 1, 3], 
                [3, 2, 1, 2, 1, 3], 
                [3, 2, 2, 2, 1, 3], 
                [3, 3, 3, 1, 3, 3]])

ex10 = np.array([[3, 3, 3, 3, 3], 
                 [3, 1, 1, 1, 3], 
                 [3, 1, 2, 1, 1],
                 [3, 1, 1, 1, 3],
                 [3, 3, 3, 3, 3]])

ex11= np.array([[3,3,5,3,3,3],
                [3,1,1,6,1,3],
                [3,1,2,1,3,3],
                [3,1,3,3,3,3]])

ex12= np.array([[3,3,5,3,3,3],
                [3,1,1,6,1,3],
                [3,1,2,1,3,3],
                [3,1,1,3,3,3]])
