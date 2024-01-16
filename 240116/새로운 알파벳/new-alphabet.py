from collections import deque

n = int(input())
words = [input() for _ in range(n)]

nodes = set()
for word in words:
    nodes |= set(word)

q = deque()

edges = {node: [] for node in nodes}
indegree = {node: 0 for node in nodes}
visited = {node: False for node in nodes}

answer = ''
is_inf = False

for i in range(n - 1):
    word1, word2 = words[i], words[i + 1]
    j = 0
    while j < min(len(word1), len(word2)):
        if (a := word1[j]) != (b := word2[j]):
            if b not in edges[a]:
                edges[a].append(b)
                indegree[b] += 1
            break
        else:
            j += 1

for node in nodes:
    if not indegree[node]:
        q.append(node)

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