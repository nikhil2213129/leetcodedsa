class Solution(object):
    def countOperations(self, num1, num2):
        def function(x,y,count):
            if x == 0 or y == 0:
                return count
            q,r = divmod(x,y)
            return function(y,r,count+q)
        return function(num1,num2,0)
        
