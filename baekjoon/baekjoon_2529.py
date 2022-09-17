# https://www.acmicpc.net/problem/2529
# 백준 2529 : 부등호
# LEVEL : Silver 1

from socketserver import ThreadingUDPServer
import sys
from itertools import permutations



def solution():
    k = int(sys.stdin.readline())
    signs = sys.stdin.readline().rstrip().split()
    
    visited = [False] * 10
    answer = []

    def correct(x, y, op):
        if op == '<':
            return x < y
        else:
            return x > y

    def find(index, number):
        if index == k+1:
            answer.append(number)
            return
        
        for i in range(10):
            if not visited[i] and \
                (index == 0 or correct(number[index-1], str(i), signs[index-1])):
                visited[i] = True
                find(index + 1, number + str(i))
                visited[i] = False

    
    find(0, "")

    print(answer[-1])
    print(answer[0])


solution()
