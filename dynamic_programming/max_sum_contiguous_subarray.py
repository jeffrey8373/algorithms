import numpy as np

MaxHere = [-1,-1,-1,-1,-1,-1,-1]
def dp_maxhere(A,i):
    if i == 0:
        return max(A[i],0)
    if i > 1:
        return max(MaxHere[i-1] + A[i],0)


if __name__ == '__main__':
    A = [-2, 5, -1, -5, 3, -1, 2]
    dp_maxhere(A,6)