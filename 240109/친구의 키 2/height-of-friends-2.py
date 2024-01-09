n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1

if n == sum(indegree):
    print('Consistent')
else:
    print('Inconsistent')