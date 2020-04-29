import numpy as np

MaxHere = [-1,-1,-1,-1,-1,-1,-1]

def dp_maxhere(A,i):
    if i == 0:
        MaxHere[i] = max(A[i],0)
        return MaxHere[i]
    if i > 0:
        MaxHere[i]= max(dp_maxhere(A,i-1) + A[i],0)
        return MaxHere[i]


if __name__ == '__main__':
    A = [2, -6, -1, 3, -1, 2, -2]
    dp_maxhere(A,6)
    print(MaxHere)