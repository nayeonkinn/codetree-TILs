from collections import deque

n, m1, m2 = map(int, input().split())

edges = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
q = deque()
route = []

for _ in range(m1):
    a, b = map(int, input().split())
    edges[a].append(b)
    indegree[b] += 1

for _ in range(m2):
    input()

for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)

while q:
    x = q.popleft()
    route.append(x)

    for y in edges[x]:
        indegree[y] -= 1

        if not indegree[y]:
            q.append(y)

if len(route) == n:
    print('Yes')
else:
    print('No')