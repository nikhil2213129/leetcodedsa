class Solution(object):
    def getHappyString(self, n, k):
        chars = ['a', 'b', 'c']
        res = []
        def dfs(path):
            if len(path) == n:
                res.append("".join(path))
                return
            for ch in chars:
                if not path or path[-1] != ch:
                    dfs(path + [ch])
        dfs([])
        res.sort()
        return res[k-1] if k <= len(res) else ""

        
