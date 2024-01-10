from collections import deque

n, m = map(int, input().split())

edges = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
visited = [False] * (n + 1)
q = deque()

for _ in range(m):
    a, _ = map(int, input().split())
    for b in map(int, input().split()):
        edges[b].append(a)
        indegree[a] += 1

input()

for piece in list(map(int, input().split())):
    q.append(piece)
    visited[piece] = True

while q:
    x = q.popleft()

    for y in edges[x]:
        if visited[y]:
            continue

        indegree[y] -= 1

        if not indegree[y]:
            q.append(y)
            visited[y] = True

answer = [i for i, v in enumerate(visited) if v]
print(len(answer))
print(*answer)