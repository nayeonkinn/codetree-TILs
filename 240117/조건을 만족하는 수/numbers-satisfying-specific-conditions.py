import heapq

n = int(input())
signs = input().split()

edges = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for i in range(n - 1):
    if signs[i] == '<':
        edges[i + 1].append(i + 2)
    else:
        edges[i + 2].append(i + 1)

def topological_sort(reverse):
    pq = []
    answer = []

    for i in range(1, n + 1):
        for x in edges[i]:
            indegree[x] += 1

    for i in range(1, n + 1):
        if not indegree[i]:
            heapq.heappush(pq, -i if reverse else i)
    
    while pq:
        x = heapq.heappop(pq) * (-1 if reverse else 1)
        answer.append(x)

        for y in edges[x]:
            indegree[y] -= 1

            if not indegree[y]:
                heapq.heappush(pq, -y if reverse else y)

    answer2 = [0] * n

    for i in range(n):
        answer2[answer[i] - 1] = i + 1

    for num in answer2:
        print(f'{num:03d}', end='')
    print()

topological_sort(False)
topological_sort(True)