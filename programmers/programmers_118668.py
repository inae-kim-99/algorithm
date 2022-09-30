# https://school.programmers.co.kr/learn/courses/30/lessons/118668
# programmers 118668 : 코딩 테스트 공부
# LEVEL : 3

def solution(alp, cop, problems):
    max_alp_req, max_cop_req = 0, 0
    for p in problems:
        max_alp_req = max(max_alp_req, p[0])
        max_cop_req = max(max_cop_req, p[1])

    alp = min(alp, max_alp_req)
    cop = min(cop, max_cop_req)

    dp = [[float('inf') for _ in range(max_cop_req + 1)]
          for _ in range(max_alp_req + 1)]
    dp[alp][cop] = 0

    for i in range(alp, max_alp_req + 1):
        for j in range(cop, max_cop_req + 1):
            if i + 1 <= max_alp_req:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j + 1 <= max_cop_req:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    next_alp = min(max_alp_req, i + alp_rwd)
                    next_cop = min(max_cop_req, j + cop_rwd)
                    dp[next_alp][next_cop] = min(
                        dp[next_alp][next_cop], dp[i][j] + cost)

    answer = dp[-1][-1]

    return answer
