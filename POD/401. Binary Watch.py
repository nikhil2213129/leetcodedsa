class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        ans = []
        for i in range(12):
            for j in range(60):
                if bin(i)[2:].count("1") + bin(j)[2:].count("1") == turnedOn:
                    t = "{}:{:02d}".format(i, j)  # <-- fixed formatting
                    ans.append(t)
        return ans
