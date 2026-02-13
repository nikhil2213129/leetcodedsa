class Solution(object):
    def longestBalanced(self, s):
        n = len(s)
        if n == 0: return 0
    
        seen3 = {(0, 0): -1}
        a = b = c = 0
        max_len = 0
        for i, ch in enumerate(s):
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else:  # 'c'
                c += 1
            key = (a - b, b - c)
            if key in seen3:
                max_len = max(max_len, i - seen3[key])
            else:
                seen3[key] = i
    
        pairs = [('a', 'b'), ('a', 'c'), ('b', 'c')]
        for x, y in pairs:
            seen = {0: -1} 
            diff = 0
            idx = -1       
            for ch in s:
                if ch == x:
                    idx += 1
                    diff += 1
                    if diff in seen:
                        max_len = max(max_len, idx - seen[diff])
                    else:
                        seen[diff] = idx
                elif ch == y:
                    idx += 1
                    diff -= 1
                    if diff in seen:
                        max_len = max(max_len, idx - seen[diff])
                    else:
                        seen[diff] = idx
                else:
                    seen = {0: -1}
                    diff = 0
                    idx = -1
    
        run_len = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                run_len += 1
            else:
                max_len = max(max_len, run_len)
                run_len = 1
        max_len = max(max_len, run_len)
    
        return max_len
