import heapq

n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
q = []

for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    indegree[b] += 1

for i in range(1, n + 1):
    edges[i].sort()
    if not indegree[i]:
        heapq.heappush(q, i)

while q:
    x = heapq.heappop(q)
    print(x, end=' ')

    for y in edges[x]:
        indegree[y] -= 1

        if not indegree[y]:
            heapq.heappush(q, y)