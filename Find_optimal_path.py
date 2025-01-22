#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:40:45 2024

@author: bzhao43
"""
import numpy as np

def max_path_sum(a):
    n = len(a)
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = a[0][0]

    # calculate dp array
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                dp[i][j] = dp[i][j-1] + a[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + a[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + a[i][j]

    # find the maximum path
    max_path = []
    i, j = n-1, n-1
    while i >= 0 and j >= 0:
        max_path.append(a[i][j])
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1

    max_path.reverse()
    return dp[n-1][n-1], max_path

# Show an example
a = [[0, 0, 0,0],
     [0.2, 0.2, 0.2,0.2],
     [1.1, 1.3, 1.3,1.3],
     [1.6, 1.9, 1.9,1.9]]
max_sum, max_path = max_path_sum(a)
print("The summer of the maxium path:", max_sum)
print("Maxium path:", max_path)


##Air Heatwave
metrix1=np.load("air_heatwave_matrix.npy")

metrix1=np.flip(np.flip(metrix1,0),1)

max_sum, max_path = max_path_sum(metrix1)
print("The summer of the maxium path:", max_sum)
print("Maxium path:", max_path)

##Lake Heatwave
metrix2=np.load("lakehw.npy")

metrix2=np.flip(np.flip(metrix2,0),1)
max_sum, max_path = max_path_sum(metrix2)
print("The summer of the maxium path:", max_sum)
print("Maxium path:", max_path)

