n = int(input())
nums = list(map(int, input().split()))

max = 0

nums.sort()

for i in range(n):
    if nums[i] + nums[2*n-1-i] > max:
        max = nums[i] + nums[2*n-1-i]

print(max)
