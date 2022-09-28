# https://www.acmicpc.net/problem/1759
# 백준 1759 : 암호 만들기
# LEVEL : Gold 5

import sys
input = sys.stdin.readline

def solution():
    VOWEL = ['a', 'e', 'i', 'o', 'u']

    L, C = map(int, input().split())
    chars = input().rstrip().split()
    chars.sort()

    visited = [False] * C

    passwords = []

    def dfs(pw, idx, vowel_cnt): 
        if len(pw) == L:
            if 0 < vowel_cnt <= L-2: # pw의 모음이 1개~L-2개인 경우 (-> 모음이 L-2개 이하이면 자음은 최소 2개 이상이 됨.)
                passwords.append(pw)
            return
        if idx == C: # 문자의 종류를 모두 확인한 경우
            return

        for i in range(idx, C): # (idx : 이전에 추가한 문자의 위치 + 1) 부터 추가할 수 있도록 한다. (사전순)
            if not visited[i]:
                visited[i] = True
                if chars[i] in VOWEL:
                    dfs(pw + chars[i], i + 1, vowel_cnt + 1)
                else:
                    dfs(pw + chars[i], i + 1, vowel_cnt)
                visited[i] = False
        
    dfs("", 0, 0)

    for password in passwords:
        print(password)
        

solution()