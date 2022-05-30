# https://www.acmicpc.net/problem/1912
# baekjoon 1912 : 연속합
# LEVEL : 실버2

length = int(input())
nums = list(map(int, input().split()))

for i in range(1, length):
    if nums[i-1] > 0:
        nums[i] += nums[i-1]

print(max(nums))