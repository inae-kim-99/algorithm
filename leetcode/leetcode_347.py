# https://leetcode.com/problems/top-k-frequent-elements/
# leetcode 347 : Top K Frequent Elements
# LEVEL : Medium

import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        answer = []
        
        for num, _ in c.most_common(k):
            answer.append(num)
            
        return answer