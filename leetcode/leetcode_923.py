# https://leetcode.com/problems/3sum-with-multiplicity/
# leetcode 923 : 3Sum With Multiplicity
# LEVEL : Medium

import collections
import itertools

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        maximum = 10**9 + 7
        c = collections.Counter(arr)
        answer = 0
        
        for i, j in itertools.combinations_with_replacement(c, 2):
            k = target - i - j
            if i == j == k:
                answer += (c[i] * (c[j] - 1) * (c[k] - 2) / 6) % maximum
            elif i == j != k:
                answer += (c[i] * (c[j] - 1) * c[k] / 2) % maximum
            elif k > i and k > j:
                answer += (c[i] * c[j] * c[k]) % maximum
        
        return int(answer)