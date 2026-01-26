class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        diff = float('inf')   # Start with infinity
        res = []
        
        for i in range(1, len(arr)):
            current_diff = arr[i] - arr[i-1]
            if current_diff < diff:
                diff = current_diff
                res = [[arr[i-1], arr[i]]]  # reset with new min pair
            elif current_diff == diff:
                res.append([arr[i-1], arr[i]])  # add another min pair
        return res
