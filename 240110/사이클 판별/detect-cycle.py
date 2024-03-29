from collections import deque

n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
q = deque()
order = []

for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    indegree[b] += 1

for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)

while q:
    x = q.popleft()
    order.append(x)

    for y in edges[x]:
        indegree[y] -= 1

        if not indegree[y]:
            q.append(y)

if len(order) == n:
    print('Not Exists')
else:
    print('Exists')