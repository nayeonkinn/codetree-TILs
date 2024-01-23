import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

edges = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

q = []
answer = [0] * (n + 1)

# outdegree가 0인 노드 중 가장 번호가 큰 노드를 n번째에 매핑 -> 뒤집어서 연산
for _ in range(m):
    x, y = map(int, input().split())
    edges[y].append(x)
    indegree[x] += 1

for i in range(1, n + 1):
    if not indegree[i]:
        heapq.heappush(q, -i)

cnt = n
while q:
    x = -heapq.heappop(q)

    answer[x] = cnt
    cnt -= 1

    for y in edges[x]:
        indegree[y] -= 1

        if not indegree[y]:
            heapq.heappush(q, -y)

if all(answer[1:]):
    print(*answer[1:])
else:
    print(-1)