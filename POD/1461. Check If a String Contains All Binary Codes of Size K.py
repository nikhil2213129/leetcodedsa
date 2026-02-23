class Solution(object):
    def hasAllCodes(self, s, k):
        needed = 1 << k
        if len(s) < k + needed - 1:
            return False

        seen = [False] * needed
        mask = needed - 1
        curr = 0
        count = 0

        for i, ch in enumerate(s):
            curr = ((curr << 1) & mask) | (ch == '1')

            if i >= k - 1:
                if not seen[curr]:
                    seen[curr] = True
                    count += 1
                    if count == needed:
                        return True

        return False
