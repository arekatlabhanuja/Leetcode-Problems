# How to check if a given array represents a Binary Heap?
# Input:  arr[] = {90, 15, 10, 7, 12, 2} 
# Output: True
# The given array represents below tree
#        90
#      /    \
#    15      10
#   /  \     /
#  7    12  2 
# The tree follows max-heap property as every
# node is greater than all of its descendants.

# Python3 program to check whether a
# given array represents a max-heap or not
 
# Returns true if arr[i..n-1]
# represents a max-heap
def isHeap(arr, n):
     
    # Start from root and go till
    # the last internal node
    for i in range(int((n - 2) / 2) + 1):
         
        # If left child is greater,
        # return false
        if arr[2 * i + 1] > arr[i]:
                return False
 
        # If right child is greater,
        # return false
        if (2 * i + 2 < n and
            arr[2 * i + 2] > arr[i]):
                return False
    return True