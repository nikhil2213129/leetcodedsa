'''
def to_matrix(array, rows, cols):
    return [array[i*cols:(i+1)*cols] for i in range(rows)]

class Solution(object):
    def rangeAddQueries(self, n, queries):
        d = {}
        result = []

        # initialize matrix dictionary
        for i in range(n):
            for j in range(n):
                d[str([i,j])] = 0

        # process each query
        for q in queries:
            row1, col1, row2, col2 = q
            a = []
            for x in range(row1, row2+1):
                for y in range(col1, col2+1):
                    a.append([x,y])
            a = [str(i) for i in a]
            for i in a:
                d[i] += 1
        for i in range(n):
            for j in range(n):
                result.append(d[str([i, j])])
        a = to_matrix(result, n, n)
        return a
'''
class Solution(object):
    def rangeAddQueries(self, n, queries):
        # initialize difference matrix
        diff = [[0]*(n+1) for _ in range(n+1)]

        # apply each query using corner updates
        for row1, col1, row2, col2 in queries:
            diff[row1][col1] += 1
            diff[row1][col2+1] -= 1
            diff[row2+1][col1] -= 1
            diff[row2+1][col2+1] += 1

        # build result with prefix sums
        result = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                val = diff[i][j]
                if i > 0: val += result[i-1][j]
                if j > 0: val += result[i][j-1]
                if i > 0 and j > 0: val -= result[i-1][j-1]
                result[i][j] = val

        return result
