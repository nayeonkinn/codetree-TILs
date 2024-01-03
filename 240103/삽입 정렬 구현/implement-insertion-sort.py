n = int(input())
nums = list(map(int, input().split()))

def insertion_sort():
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

insertion_sort()

print(*nums)