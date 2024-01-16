from collections import defaultdict, deque

n = int(input())
words = [input() for _ in range(n)]

alpha = set()
for word in words:
    alpha |= set(word)

q = deque()
edges = defaultdict(list)
indegree = defaultdict(int)

order = ''

cnt = 0
for i in range(n - 1):
    word1, word2 = words[i], words[i + 1]
    idx = 0
    while idx < min(len(word1), len(word2)):
        if (a := word1[idx]) != (b := word2[idx]):
            edges[a].append(b)
            indegree[b] += 1
            cnt += 1
            break
        else:
            idx += 1

for a in alpha:
    if not indegree[a]:
        q.append(a)

while q:
    a = q.popleft()
    order += a

    for b in edges[a]:
        indegree[b] -= 1

        if not indegree[b]:
            q.append(b)

if cnt < len(alpha) - 1:
    print('inf')
elif len(order) == len(alpha):
    print(order)
else:
    print(-1)