from collections import deque

n = int(input())
words = [input() for _ in range(n)]

alpha = set()
for word in words:
    alpha |= set(word)

q = deque()

edges = {x: [] for x in alpha}
indegree = {x: 0 for x in alpha}
visited = {x: False for x in alpha}

answer = ''
is_inf = False

for i in range(n - 1):
    for j in range(0, min(len(words[i]), len(words[i + 1]))):
        a = words[i][j]
        b = words[i + 1][j]
        if a != b:
            if b not in edges[a]:
                edges[a].append(b)
                indegree[b] += 1
            break

for x in alpha:
    if not indegree[x]:
        q.append(x)

while q:
    if len(q) > 1:
        is_inf = True

    x = q.popleft()
    visited[x] = True
    answer += x

    for y in edges[x]:
        indegree[y] -= 1

        if not indegree[y]:
            q.append(y)

is_cycle = not all(visited.values())

if is_cycle:
    print(-1)
elif is_inf:
    print('inf')
else:
    print(answer)