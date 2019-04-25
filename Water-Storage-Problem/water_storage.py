import numpy as np

# Generates neighbors of the position (i,j) from a given matrix
def get4Neighbors(i,j,mat):
    nbr = np.empty(4)
    nbr[0] = mat[i-1][j]
    nbr[1] = mat[i][j-1]
    nbr[2] = mat[i][j+1]
    nbr[3] = mat[i+1][j]
    return nbr


# Generates a drain_possibility matrix where 1's denote water storing capability and 0's otherwise
def checkDrainPossibility(platform): 
    n,m = platform.shape
    platform1 = np.empty([n,m], dtype=int)
    platform1[:] = platform[:] # Copying only values of the given matrix to another without of the reference. 
                               # This will not modified the original matrix when any changes are made on the copied matrix.
    platform1_d = np.ones([n,m], dtype=int) # This is a drain_possibility matrix
    
    un, cnt = np.unique(platform1, return_counts =True, axis=None)
    maximum = un[cnt.argmax()]
    if(maximum != un[len(un)-1]):
        for i in range(0,n):
            for j in range(0,m):
                if(platform1[i][j]>maximum):
                    platform1[i][j]= maximum   

    print("Smoothened platform after cutting off extra elevations")
    print(platform1)
         
    diff = np.empty(8) # empty list to hold neighbors of the given matrix
    diff_d = np.empty(8) # empty list to hold neighbors of the drain_possibility matrix
    
    # Making all boundary elements of drain_possibility matrix 0's, as they cannot hold water
    for i in range(n): 
        for j in range(m): 
            if (i == 0): 
                platform1_d[i][j] = 0 
            elif (i == n-1): 
                platform1_d[i][j] = 0 
            elif (j == 0): 
                platform1_d[i][j] = 0 
            elif (j == m-1): 
                platform1_d[i][j] = 0

    if((n > 2) and (m>2)): 
      #traverse through each cell other than boundaries and determine the drain_possibility
      for i in range(1,(n-1)):
        for j in range(1,(m-1)):
            if (platform1[i][j] == 0): # step 5.A
                platform1_d[i][j] = 0
            
            else:
                diff = get4Neighbors(i,j,platform1)
                diff_d = get4Neighbors(i,j,platform1_d)

                if 0 in diff: # step 5.C
                    platform1_d[i][j] = 0
                
                elif 0 in diff_d: # step 5.B + 5.D
                    drain = 0
                    for idx, k in enumerate(diff_d): 
                        if k == 0:
                            if platform1[i][j] >= diff[idx]:
                                drain += 1
                    if drain > 0:
                        platform1_d[i][j] = 0
                
                else: # step 5.D
                    drain = 0
                    for idx, k in enumerate(diff):
                        if platform1[i][j] >= diff[idx]:
                            drain += 1
                    if drain == 4:
                        platform1_d[i][j] = 0
                        
            #print('')
            #print(platform1_d)
 
    else:
        print("platform cannot hold water")
    
    # update the drain_possibility matrix by traversing all the positions containing 1's. 
    # This step is required to determine hidden drain possibilities which were determined as 1's(false positives) in the previous loop.
    def recheck():
        change = 0
        if((n > 2) and (m>2)): 
            for i in range(1,(n-1)):
                for j in range(1,(m-1)):
                    
                    if (platform1_d[i][j] != 0):
                        diff = get4Neighbors(i,j,platform1)
                        diff_d = get4Neighbors(i,j,platform1_d)
                        if 0 in diff_d:
                            drain = 0
                            for idx, k in enumerate(diff_d):
                                if k == 0:
                                    if platform1[i][j] >= diff[idx]:
                                        drain += 1
                            if drain > 0:
                                platform1_d[i][j] = 0
                                change += 1
                                
        if change > 0:
            recheck()
                            
                
    recheck()
    print('')
    print('Dummy matrix that shows water storage possibility of each position. 1: Storage possible; 2: Drain')
    print(platform1_d)
    return platform1, platform1_d


def WaterStoredInPlatform(platform):
    n,m = platform.shape
    platform1, platform1_d = checkDrainPossibility(platform)

    diff = np.empty(8)
    diff_d = np.empty(8)
    waterstored = 0

    if((n > 2) and (m>2)): 
        for i in range(1,(n-1)):
            for j in range(1,(m-1)):
            
                if (platform1_d[i][j] != 0):
                    diff = get4Neighbors(i,j,platform1)
                    diff_d = get4Neighbors(i,j,platform1_d)
                    
                    support = []
                    for idx, k in enumerate(diff_d):
                        if k == 0:
                            support.append(diff[idx])
                    
                    platform1_d[i][j] = min(support)-platform1[i][j]
                    
        print('')
        print('Dummy matrix with water storage capacity of each position')
        print(platform1_d)
        print('')
        waterstored = platform1_d.sum()
                        
          
    else:
        print("Platform cannot hold water")
                
    return print('Total amount of water that can be stored in given platform is {}' .format(waterstored))
