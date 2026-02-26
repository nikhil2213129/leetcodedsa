class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int

        def converttodecimal(binary):
            length = len(binary)
            curr = 0
            decimal = 0
            while length>0:
                decimal += (2**(length-1))*(int(binary[curr]))
                curr = curr + 1
                length -= 1
            return decimal
        """
        d = int(s,2)
        count = 0
        while d!=1:
            if d&1:
                d += 1
            else:
                d >>= 1
            count += 1
        return count
        
