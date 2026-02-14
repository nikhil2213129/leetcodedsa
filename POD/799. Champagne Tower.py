class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        query_glass = min(query_glass, query_row - query_glass)
        glass = [0.] * (query_glass + 1)
        glass[0] = float(poured)
        c = query_row - query_glass + 1
        z = -1

        for i in xrange(query_row):
            mid = i >> 1
            if mid >= query_glass:
                mid, i1 = query_glass, 0
            else:
                i1 = i & 1
            excess = max(glass[mid] - 1., 0.)
            if excess:
                if i1 != 0:
                    glass[mid + 1] += excess
                glass[mid] = excess * .5
            else:
                return 0.
            for j in xrange(mid - 1, max(-1, i - c, z), -1):
                excess = max(glass[j] - 1., 0.) * .5
                if excess:
                    glass[j + 1] += excess
                    glass[j] = excess
                else:
                    z = j
                    break

        return min(1., glass[query_glass])
