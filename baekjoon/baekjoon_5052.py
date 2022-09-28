# https://www.acmicpc.net/problem/5052
# 백준 5052 : 전화번호 목록
# LEVEL : Gold 4

import sys
input = sys.stdin.readline

def solution():
    TC = int(input())

    for _ in range(TC):
        N = int(input())
        numbers = [input().rstrip() for _ in range(N)]
        numbers.sort()
        calls = {} # 전화번호 목록

        for number in numbers:
            for i in range(1, len(number)+1): # 숫자를 하나씩 추가하면서 calls에 있는지 확인한다.
                if calls.get(number[:i]): # 있다면 전화가 걸려버리기 때문에 break
                    break
            else: # 모두 확인했는데 없으면 현재 전화번호를 calls에 저장한다.
                calls[number] = True
            
            # 위 else문이 실행되지 않은 경우 중간에 전화가 걸린 것이기 때문에 NO
            if calls.get(number) == None: 
                print("NO")
                break
        else: # 위 경우에서 break되지 않은 경우 YES
            print("YES")


solution()