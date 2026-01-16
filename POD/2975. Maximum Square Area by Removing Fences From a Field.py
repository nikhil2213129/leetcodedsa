class Solution:
    def maximizeSquareArea(self, totalHeight, totalWidth, horizontalCuts, verticalCuts):
        MOD = 10**9 + 7

        def prep(cuts, limit):
            cuts = sorted(cuts)
            return [1] + cuts + [limit]

        h = prep(horizontalCuts, totalHeight)
        v = prep(verticalCuts, totalWidth)

        gapSet = set()

        for i in range(len(h)):
            for j in range(i+1, len(h)):
                gapSet.add(h[j]-h[i])

        best = 0
        for i in range(len(v)):
            for j in range(i+1, len(v)):
                d = v[j]-v[i]
                if d > best and d in gapSet:
                    best = d

        return -1 if best == 0 else (best*best) % MOD
