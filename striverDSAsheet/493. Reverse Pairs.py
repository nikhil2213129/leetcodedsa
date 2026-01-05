class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return mergesort_and_count(nums, 0, len(nums) - 1)
        
def merge(A, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
    L = A[start:start + n1]
    R = A[mid + 1:mid + 1 + n2]
    i = j = 0
    for k in range(start, end + 1):
        if j >= n2 or (i < n1 and L[i] <= R[j]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def mergesort_and_count(A, start, end):
    if start < end:
        mid = (start + end) // 2
        count = mergesort_and_count(A, start, mid) + mergesort_and_count(A, mid + 1, end)
        j = mid + 1
        for i in range(start, mid + 1):
            while j <= end and A[i] > 2 * A[j]:
                j += 1
            count += j - (mid + 1)
        merge(A, start, mid, end)
        return count
    else:
        return 0
