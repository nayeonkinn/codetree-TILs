MAX_LEN = 6
MAX_DIGIT = 10

n = int(input())
nums = list(map(int, input().split()))

def radix_sort():
    global nums

    p = 1
    for pos in range(MAX_LEN):
        temp = [[] for _ in range(MAX_DIGIT)]
        for num in nums:
            digit = (num // p) % 10
            temp[digit].append(num)

        nums = []
        for digit in range(MAX_DIGIT):
            for num in temp[digit]:
                nums.append(num)
        
        p *= 10

radix_sort()

print(*nums)