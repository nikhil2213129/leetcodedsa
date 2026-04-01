class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        """
        :type positions: List[int]
        :type healths: List[int]
        :type directions: str
        :rtype: List[int]
        """
    # Stack : Time O(n) Space O(n)
        index_m = {p: i for i, p in enumerate(positions)}
        stack = []
        for p in sorted(positions):
            i = index_m[p]
            if directions[i] == "R":
                stack.append(i)
            else:
                while stack and healths[i] > 0:
                    i2 = stack.pop()
                    if healths[i] > healths[i2]:
                        healths[i2] = 0
                        healths[i] -= 1 
                    elif healths[i] < healths[i2]:
                        healths[i2] -= 1
                        healths[i] = 0
                        stack.append(i2)
                    else:
                        healths[i2] = 0
                        healths[i] = 0
        return [h for h in healths if h > 0]
        
