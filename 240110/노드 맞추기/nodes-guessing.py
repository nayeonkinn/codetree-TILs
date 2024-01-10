from collections import deque 

n = int(input())
nodes = sorted(input().split())
m = int(input())

descendant = {node: [] for node in nodes}
child = {node: [] for node in nodes}
indegree = {node: 0 for node in nodes}

q = deque()

for _ in range(m):
    x, y = input().split()
    descendant[y].append(x)
    indegree[x] += 1

for node in nodes:
    if not indegree[node]:
        q.append(node)

print(len(q))
print(*q)

while q:
    x = q.popleft()

    for y in descendant[x]:
        indegree[y] -= 1

        if not indegree[y]:
            q.append(y)
            child[x].append(y)

for k, v in child.items():
    print(k, len(v), *sorted(v))