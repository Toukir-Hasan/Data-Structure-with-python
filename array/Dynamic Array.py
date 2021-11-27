

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    lastanswer=0
    arr=[]
    result=[]
    for x in range(0,n):
        arr.append([])
    for y in range(0,len(queries)):
        if queries[y][0]==1:
            arr[(queries[y][1]^lastanswer)%n].append(queries[y][2])
        else:
            if len(queries[y])==0:
                pass
            else:
                a=(queries[y][1]^lastanswer)%n
                lastanswer=arr[a][queries[y][2]%len(arr[a])]
                result.append(lastanswer)
    return result

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)
    print(result)
