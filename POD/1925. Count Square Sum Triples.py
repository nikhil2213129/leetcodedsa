class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        a = {i**2 for i in range(1,n+1)}
        for i in range(1,n+1):
            t = i*i
            for j in range(1,n+1):
                s = t+j*j
                if s in a:
                    count +=1
        return count
                    
        
