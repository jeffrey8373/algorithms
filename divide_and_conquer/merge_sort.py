# give an array sort it
import math

layer_left = 0
layer_right = 0
# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
def merge(array,left,mid,right):
    # the elements in the left
    n1 = mid - left + 1
    # the elements in the right
    n2 = right - mid + 1

    # initial 2 arrays
    R = [0] * n1
    L = [0] * n1

    #copy data to R and L
    for i in range(left,mid):
        L[i] = array[left + i]
    for i in range(mid,right):
        R[i] = array[mid + i]

    # merge
    i=0
    j=0
    k = left
    while (i < n1) and (j < n2):
        if L[i] < R[i]:
            array[k] = L[i]
            i +=1
        else:
            array[k] = R[i]
        k +=1

    # copy the remaining elements
    # while i < n1:
    #     array[k] = L[i]
    #     i += 1
    #     k += 1




def merge_sort(array,left,right):
    global layer_left
    global layer_right
    if(left<right):

        mid = math.floor((left+right)/2)

        layer_left = layer_left + 1
        merge_sort(array, left, mid)

        layer_right = layer_right + 1
        merge_sort(array, mid, right)

        #conquer
        merge(array,left,mid,right)



if __name__ == '__main__':
    # Driver code to test above
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)
    print("Given array is")
    for i in range(n):
        print("%d" % arr[i]),

    merge_sort(arr, 0, n - 1)
    print("\n\nSorted array is")
    for i in range(n):
        print("%d" % arr[i]),
