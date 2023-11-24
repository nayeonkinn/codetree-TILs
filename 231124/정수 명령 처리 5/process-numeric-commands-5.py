n = int(input())

arr = []

for _ in range(n):
    command, *num = input().split()
    
    if command == 'push_back':
        arr.append(int(num[0]))
    elif command == 'pop_back':
        arr.pop()
    elif command == 'size':
        print(len(arr))
    else:
        print(arr[int(num[0]) - 1])