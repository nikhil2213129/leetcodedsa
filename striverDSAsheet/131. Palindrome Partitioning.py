class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        res = []
        def isPalindrome(sub):
            return sub == sub[::-1]
        def getpartition(start,path):
            if start == n:
                res.appe10nd(path[:])
            for end in range(start+1,n+1):
                left = s[start:end]
                if isPalindrome(left):
                    path.append(left)
                    getpartition(end,path)
                    path.pop()
        getpartition(0,[])
        return res
