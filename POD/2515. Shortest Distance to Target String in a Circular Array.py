class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        n = len(words)
        s = startIndex
        for i in range((n >> 1) + 1):
            if ((words[(s + i) % n] == target) |
                (words[(s - i) % n] == target)):
                return i
        return -1
