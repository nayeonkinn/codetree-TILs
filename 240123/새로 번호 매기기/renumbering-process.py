import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

edges = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

q = []
route = []

for _ in range(m):
    x, y = map(int, input().split())
    edges[x].append(y)
    indegree[y] += 1

for i in range(1, n + 1):
    if not indegree[i]:
        heapq.heappush(q, i)

while q:
    x = heapq.heappop(q)
    route.append(x)

    for y in edges[x]:
        indegree[y] -= 1

        if not indegree[y]:
            heapq.heappush(q, y)

if len(route) != n:
    print(-1)
else:
    answer = [0] * n
    for i, v in enumerate(route):
        answer[v - 1] = i + 1
    print(*answer)