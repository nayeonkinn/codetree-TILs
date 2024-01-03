n = int(input())
nums = input().split()

def radix_sort(nums):
    for i in range(len(nums[0])):
        temp = [[] for _ in range(10)]

        for num in nums:
            temp[int(num[i])].append(num)
                
        new_nums = []
        for j in range(10):
            for k in temp[j]:
                new_nums.append(k)

        nums = new_nums
    
    return nums

print(*radix_sort(nums))