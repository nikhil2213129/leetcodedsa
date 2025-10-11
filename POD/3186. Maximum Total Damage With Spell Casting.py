class Solution(object):
    def maximumTotalDamage(self, power):
        freq_map = {}
        for val in power:
            if val in freq_map:
                freq_map[val] += 1
            else:
                freq_map[val] = 1
        unique = sorted(freq_map.keys())
        n = len(unique)
        damage = [unique[i] * freq_map[unique[i]] for i in range(n)]
        dp = [0] * n
        for i in range(n):
            take = damage[i]
            j = i - 1
            while j >= 0 and unique[j] > unique[i] - 3:
                j -= 1
            if j >= 0:
                take += dp[j]

            skip = dp[i - 1] if i > 0 else 0
            dp[i] = max(take, skip)
        return dp[-1]
a = Solution()
print(a.maximumTotalDamage([7,1,6,6]))

        
