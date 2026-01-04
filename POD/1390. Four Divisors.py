class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in nums:
            divisors = []
            for j in range(1,int(i**0.5)+1):
                if i%j == 0:
                    divisors.append(j)
                    if j != i//j:
                        divisors.append(i//j)
            if len(divisors) == 4:
                result += sum(divisors)
        return result
        
            
           
