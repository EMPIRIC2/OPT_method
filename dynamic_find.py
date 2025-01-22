#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:40:45 2024

@author: bzhao43
"""

def max_path_sum(a):
    n = len(a)
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = a[0][0]

    # 计算 dp 数组
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

    # 还原最大路径
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

# 示例用法
a = [[0, 0, 0,0],
     [0.2, 0.2, 0.2,0.2],
     [1.1, 1.3, 1.3,1.3],
     [1.6, 1.9, 1.9,1.9]]
max_sum, max_path = max_path_sum(a)
print("最大路径和:", max_sum)
print("最大路径:", max_path)

import numpy as np

metrix1=np.load("array_file.npy")

metrix1=np.flip(np.flip(metrix1,0),1)

max_sum, max_path = max_path_sum(metrix1)
print("最大路径和:", max_sum)
print("最大路径:", max_path)

metrix2=np.load("lakehw.npy")

metrix2=np.flip(np.flip(metrix2,0),1)
max_sum, max_path = max_path_sum(metrix2)
print("最大路径和:", max_sum)
print("最大路径:", max_path)


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
# Example data

colors = ["#7f384f", "#c08e96", "#dfc8ce"]  # Red tones

# Create a colormap object
muted_red = LinearSegmentedColormap.from_list('muted_red', colors)



# Plot heatmap
plt.imshow(metrix2, cmap=muted_red)

# # Define arrow length
# arrow_length = 0.8  # Adjust the length here

# # Add arrows between cells
# for i in range(len(data)):
#     for j in range(len(data[0])):
#         if i < len(data)-1:
#             plt.arrow(j, i, 0, arrow_length, head_width=0.1, head_length=0.1, fc='k', ec='k')
#         if j < len(data[0])-1:
#             plt.arrow(j, i, arrow_length, 0, head_width=0.1, head_length=0.1, fc='k', ec='k')

# plt.show()

