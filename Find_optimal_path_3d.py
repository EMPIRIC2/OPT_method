#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:40:45 2024

@author: bzhao43
"""

def max_sum_path(a):
    n = len(a)
    # Initiate array
    dp = [[[0] * n for _ in range(n)] for _ in range(n)]
    # Initialize the path array to record the points along the path.
    path = [[[''] * n for _ in range(n)] for _ in range(n)]

    # Assign the starting value to the corresponding position in the maximum value array.
    dp[0][0][0] = a[0][0][0]
    path[0][0][0] = "(0,0,0)"

    # Update the array using dynamic programming.
    for i in range(n):
        for j in range(n):
            for k in range(n):
                max_prev = max(
                    dp[i-1][j][k] if i > 0 else 0,
                    dp[i][j-1][k] if j > 0 else 0,
                    dp[i][j][k-1] if k > 0 else 0
                )
                dp[i][j][k] = max_prev + a[i][j][k]

                if max_prev == dp[i-1][j][k]:
                    path[i][j][k] = path[i-1][j][k] + f" -> ({i},{j},{k})"
                elif max_prev == dp[i][j-1][k]:
                    path[i][j][k] = path[i][j-1][k] + f" -> ({i},{j},{k})"
                else:
                    path[i][j][k] = path[i][j][k-1] + f" -> ({i},{j},{k})"
    return dp[n-1][n-1][n-1], path[n-1][n-1][n-1]


a = [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [20, 30, 40],
        [50, 60, 70],
        [80, 90, 100]
    ],
    [
        [300, 400, 500],
        [600, 700, 800],
        [900, 1000, 1100]
    ]
]
import numpy as np
arr = np.array([[[  0,   1,   3,   6],
                 [  4,   5,   7,  10],
                 [  8,   9,  11,  14],
                 [ 12,  13,  15,  18]],

                [[  2,   6,   9,  15],
                 [  8,  10,  13,  19],
                 [ 12,  14,  17,  23],
                 [ 16,  18,  21,  27]],

                [[ 10,  15,  19,  26],
                 [ 16,  20,  23,  30],
                 [ 20,  24,  27,  34],
                 [ 24,  28,  31,  38]],

                [[ 22,  27,  31,  38],
                 [ 27,  32,  35,  42],
                 [ 31,  36,  39,  46],
                 [ 35,  40,  43,  50]]])


max_sum, max_sum_path = max_sum_path(arr)
print("The summation of maximum path：", max_sum)
print("Path：", max_sum_path)


