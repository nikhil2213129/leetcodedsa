class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        d = {}
        for i in arr:
            b = bin(i)[2:]
            c = b.count("1")
            if c not in d:
                d[c] = [i]
            else:
                d[c].append(i)
        res = []
        for i in d:
            v = sorted(d[i])
            for j in v:
                res.append(j)
        return res
                
        
