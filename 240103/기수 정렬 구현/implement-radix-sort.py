n = int(input())
nums = input().split()

def radix_sort(nums):
    for i in range(max_len - 1, -1, -1):
        temp = [[] for _ in range(10)]

        for num in nums:
            temp[int(num[i])].append(num)
                
        new_nums = []
        for j in range(10):
            for k in temp[j]:
                new_nums.append(k)

        nums = new_nums
    
    return list(map(int, nums))

max_len = len(max(nums, key=len))
nums = ['0' * (max_len - len(num)) + num if len(num) < max_len else num for num in nums]

print(*radix_sort(nums))