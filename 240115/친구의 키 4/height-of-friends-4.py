from collections import deque

def cycle(limit):
    edges = [[] for _ in range(m + 1)]
    indegree = [0] * (m + 1)
    visited = [False] * (m + 1)

    q = deque()
    
    for i in range(1, limit + 1):
        x, y = hints[i]

        edges[x].append(y)
        indegree[y] += 1
    
    for x in range(1, n + 1):
        if not indegree[x]:
            q.append(x)
        
    while q:
        x = q.popleft()
        visited[x] = True

        for y in edges[x]:
            indegree[y] -= 1

            if not indegree[y]:
                q.append(y)

    return not all(visited[1:])

n, m = map(int, input().split())
hints = [()] + [tuple(map(int, input().split())) for _ in range(m)]

answer = 0
lo, hi = 1, m

while lo <= hi:
    mid = (lo + hi) // 2

    if cycle(mid):
        hi = mid - 1
        answer = mid
    else:
        lo = mid + 1

if answer:
    print(answer)
else:
    print('Consistent')