class Solution(object):
    def maximumEnergy(self, energy, k):
        dp = [0]*len(energy)
        for i in range(len(energy)-1,-1,-1):
            if i+k<len(energy):
                dp[i] = energy[i] + dp[i+k]
            else:
                dp[i] = energy[i]
        return max(dp)
