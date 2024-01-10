from collections import deque

n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, _ = map(int, input().split())
    for b in map(int, input().split()):
        edges[b].append(a)
        indegree[a] += 1

input()
piece = set(map(int, input().split()))

q = deque()
for p in piece:
    if not indegree[p]:
        q.append(p)

while q:
    x = q.popleft()

    for y in edges[x]:
        indegree[y] -= 1

        if not indegree[y]:
            q.append(y)
            piece.add(y)

print(len(piece))
print(*piece)