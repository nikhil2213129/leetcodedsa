class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d = {}
        for w in words:
            d[w] = d.get(w, 0) + 1
        s = sorted(d.items(), key=lambda item: (-item[1], item[0]))
        return [word for word, freq in s[:k]]
