# https://programmers.co.kr/learn/courses/30/lessons/84512
# programmmers 84512 : 위클리 챌린지 - 모음사전
# LEVEL : 2

from itertools import product
def solution(word):
    alphabets = ['A', 'E', 'I', 'O', 'U']
    words = []
    for i in range(1, 6):
        for order in product(alphabets, repeat=i):
            words.append(''.join(order))
    words.sort()

    return words.index(word)+1

print(solution("EIO"))