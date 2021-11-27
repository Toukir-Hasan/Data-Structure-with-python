#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    result=[]
    for x in range(0,4):
        first = arr[x][0]+arr[x][1]+arr[x][2]+arr[x+1][1]+arr[x+2][0] + arr[x+2][1]+arr[x+2][2]
        result.append(first)
        second = arr[x][1]+arr[x][2]+arr[x][3]+arr[x+1][2]+arr[x+2][1] + arr[x+2][2]+arr[x+2][3]
        result.append(second)
        third=  arr[x][2]+arr[x][3]+arr[x][4]+arr[x+1][3]+arr[x+2][2] + arr[x+2][3]+arr[x+2][4]
        result.append(third)
        forth=  arr[x][3]+arr[x][4]+arr[x][5]+arr[x+1][4]+arr[x+2][3] + arr[x+2][4]+arr[x+2][5]
        result.append(forth)
    return max(result)



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)


