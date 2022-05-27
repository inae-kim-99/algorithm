# https://programmers.co.kr/learn/courses/30/lessons/42897
# programmers 42897 : 도둑질
# LEVEL : 4

def solution(money):
    dp = [0 for _ in range(len(money))]
    dp[0], dp[1] = money[0], max(money[0], money[1])
    for i in range(2, len(money)-1):
        dp[i] = max(dp[i-1], money[i] + dp[i-2])
        
    dp2 = [0 for _ in range(len(money))]
    dp2[0], dp2[1] = 0, money[1]
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], money[i] + dp2[i-2])
        
    return max(dp[-2], dp2[-1])