from collections import deque

def is_cycle(limit):
    edges = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    visited = [False] * (n + 1)

    q = deque()

    for i in range(1, limit + 1):
        x, y = hints[i]
        edges[x].append(y)
        indegree[y] += 1
    
    for i in range(1, n + 1):
        if not indegree[i]:
            q.append(i)

    while q:
        x = q.popleft()
        visited[x] = True

        for y in edges[x]:
            indegree[y] -= 1

            if not indegree[y]:
                q.append(y)

    return not all(visited[1:])

n, m = map(int, input().split())

hints = [()]
for _ in range(m):
    hints.append(tuple(map(int, input().split())))

answer = 0
lo, hi = 1, m

while lo <= hi:
    mid = (lo + hi) // 2

    if is_cycle(mid):
        answer = mid
        hi = mid - 1
    else:
        lo = mid + 1

if answer:
    print(answer)
else:
    print('Consistent')