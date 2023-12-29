n = int(input())
arr = list(map(int, input().split()))

flag = False
while not flag:
    flag = True
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            flag = False

print(*arr)