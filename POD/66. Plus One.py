class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ch = ""
        for i in digits:
            i = str(i)
            ch+=i
        ch = int(ch)+1
        ch = str(ch)
        ch = list(ch)
        return [int(i) for i in ch]
