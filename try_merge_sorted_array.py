# Merge two given sorted integer array A and B into a new sorted integer array.

class Solution:
    """
    @param: A: sorted integer array A
    @param: B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        A.extend(B)
        return sorted(A)
