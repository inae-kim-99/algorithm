# https://programmers.co.kr/learn/courses/30/lessons/68645
# programmers 68645 : 월간 코드 챌린지 시즌1 - 삼각 달팽이
# LEVEL : 2

def solution(n):
    triangle = [[0 for _ in range(i+1)] for i in range(n)]
    direct = [(1,0), (0,1), (-1,-1)]
    y, x, i = 0, 0, 0
    
    triangle[0][0] = 1
    for number in range(2, n*(n+1)//2+1):
        if not (0 <= y+direct[i][0] < len(triangle) and 0 <= x+direct[i][1] < len(triangle[y])) or triangle[y+direct[i][0]][x+direct[i][1]] != 0:
            i = (i + 1) % 3
        y += direct[i][0]
        x += direct[i][1]
        triangle[y][x] = number
            
    answer = []
    for row in triangle:
        answer.extend(row)
    
    return answer