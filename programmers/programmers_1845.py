# https://programmers.co.kr/learn/courses/30/lessons/1845
# programmers 1845 : 찾아라 프로그래밍 마에스터 - 폰켓몬
# LEVEL 1

def solution(nums):
    return min(len(nums)/2,  len(set(nums)))
