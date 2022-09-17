# https://www.acmicpc.net/problem/14503
# 백준 14503 : 로봇 청소기
# LEVEL : Gold 5

import sys

def solution():
    EMPTY = 0
    WALL = 1
    CLEAN = 2
    DIRECTIONS = [[-1,0],[0,1],[1,0],[0,-1]] # 북, 동, 남, 서

    N, M = map(int, sys.stdin.readline().split())
    robot_y, robot_x, robot_d = map(int, sys.stdin.readline().split())
    area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    count = 0

    while True:
        if area[robot_y][robot_x] == EMPTY:
            area[robot_y][robot_x] = CLEAN
            count += 1

        for i in range(4): 
            direction = (robot_d + 3 - i) % 4
            dy, dx = DIRECTIONS[direction]

            ny = robot_y + dy
            nx = robot_x + dx

            if area[ny][nx] == EMPTY:
                robot_d = direction
                robot_y += dy
                robot_x += dx
                break
        else:
            back_y, back_x = DIRECTIONS[(robot_d + 2) % 4]
            
            robot_y += back_y
            robot_x += back_x

            if area[robot_y][robot_x] == WALL:
                break

    print(count)           


solution()