# https://www.acmicpc.net/problem/17615
# 백준 17615 : 볼 모으기
# LEVEL : Silver 1
import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    balls = sys.stdin.readline().rstrip()

    blue = balls.count('B')
    red = N - blue
    ans = N

    part = balls.rstrip('B')
    ans = min(ans, blue - (N - len(part)))
    
    part = balls.rstrip('R')
    ans = min(ans, red - (N - len(part)))

    part = balls.lstrip('B')
    ans = min(ans, blue - (N - len(part)))

    part = balls.lstrip('R')
    ans = min(ans, red - (N - len(part)))

    print(ans)

solution()

# def solution():
#     N = int(sys.stdin.readline().rstrip())
#     balls = sys.stdin.readline().rstrip()

#     blue = balls.count("B")
#     red = N-blue
#     if N == 1 or blue == 0 or red == 0:
#         print('0')
#         return

#     count = N

#     for left in range(1, N):
#         if balls[0] != balls[left]:
#             if balls[0] == 'B':
#                 count = min(count, blue-left)
#             else:
#                 count = min(count, red-left)
#             break

#     for right in range(N-2, -1, -1):
#         if balls[N-1] != balls[right]:
#             if balls[N-1] == 'B':
#                 count = min(count, right+1-red)
#             else:
#                 count = min(count, right+1-blue)
#             break
    
#     if balls[0] == balls[N-1]:
#         count = min(count, min(blue, red))
    
#     print(count)
        
