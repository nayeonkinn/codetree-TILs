import heapq

n = int(input())
signs = input().split()

edges = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

min_q, max_q = [], []
min_answer, max_answer = [], []

for i in range(n - 1):
    if signs[i] == '<':
        edges[i + 1].append(i + 2)
        indegree[i + 2] += 1
    else:
        edges[i + 2].append(i + 1)
        indegree[i + 1] += 1

for i in range(1, n + 1):
    if not indegree[i]:
        heapq.heappush(min_q, i)
        heapq.heappush(max_q, -i)

temp = indegree[:]

while min_q:
    x = heapq.heappop(min_q)
    min_answer.append(x)

    for y in edges[x]:
        indegree[y] -= 1

        if not indegree[y]:
            heapq.heappush(min_q, y)

indegree = temp

while max_q:
    x = heapq.heappop(max_q) * -1
    max_answer.append(x)

    for y in edges[x]:
        indegree[y] -= 1

        if not indegree[y]:
            heapq.heappush(max_q, -y)

min_answer2 = [0] * n
max_answer2 = [0] * n

for i in range(n):
    min_answer2[min_answer[i] - 1] = i + 1
    max_answer2[max_answer[i] - 1] = i + 1

for num in min_answer2:
    print(f'{num:03d}', end='')
print()

for num in max_answer2:
    print(f'{num:03d}', end='')
print()