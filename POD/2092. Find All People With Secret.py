class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        res = set([0, firstPerson])
        meetings.sort(key=lambda x: x[2])
        i = 0
        while i < len(meetings):
            t = meetings[i][2]
            batch = []
            while i < len(meetings) and meetings[i][2] == t:
                batch.append(meetings[i])
                i += 1

            graph = {}
            people = set()
            for x, y, _ in batch:
                graph.setdefault(x, []).append(y)
                graph.setdefault(y, []).append(x)
                people.add(x)
                people.add(y)

            stack = [p for p in people if p in res]
            visited = set(stack)
            while stack:
                u = stack.pop()
                for v in graph.get(u, []):
                    if v not in visited:
                        visited.add(v)
                        stack.append(v)

            res |= visited

        return sorted(res)
