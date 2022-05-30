# https://www.acmicpc.net/problem/11053
# baekjoon 11053 : 가장 긴 증가하는 부분 수열
# LEVEL : 실버2

N = int(input())
nums = list(map(int, input().split()))

result = [nums[0]]
for i in range(1, N):
    if nums[i] > result[-1]:
        result.append(nums[i])
    else:
        for j in range(len(result)):
            if result[j] >= nums[i]:
                result[j] = nums[i]
                break

print(len(result))
