# https://www.acmicpc.net/problem/1058
# 백준 1058 : 친구
# LEVEL : Silver 2

import sys

def solution():
    N = int(sys.stdin.readline())
    graph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
    friends = []

    for i in range(N):
        friend = set()
        for j in range(N):
            if graph[i][j] == 'Y':
                friend.add(j)
        friends.append(friend)

    answer = 0

    for i in range(N): # 각 사람 i에 대해서
        count = friends[i]
        for j in range(N):
            if i != j and friends[i].intersection(friends[j]):
                count.add(j)
        answer = max(answer, len(count))

    print(answer)

def solution2():
    N = int(sys.stdin.readline())
    graph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
    friends = []

    for i in range(N):
        friend = set()
        for j in range(N):
            if graph[i][j] == 'Y':
                friend.add(j)
        friends.append(friend)
    answer = 0

    for person in range(N):
        count = friends[person]
        for i in range(friend):
            count.update(friends)
        answer = max(answer, len(count-set([person])))
    

    print(answer)


solution2()
