import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

edges = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

q = []
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    indegree[b] += 1

for i in range(1, n + 1):
    if not indegree[i]:
        heapq.heappush(q, i)

while q:
    x = heapq.heappop(q)
    answer.append(x)

    for y in edges[x]:
        indegree[y] -= 1

        if not indegree[y]:
            heapq.heappush(q, y)

if len(answer) == n:
    print(*answer)
else:
    print(-1)