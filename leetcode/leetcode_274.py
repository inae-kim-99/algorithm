# https://leetcode.com/problems/h-index/
# leetcode 274 : H-Index
# LEVEL : Medium

# 풀이
# h-index란, n개 이상의 논문을 가지고 있으면서 각 인용수가 n번 이상이면 h-index를 n이라고 한다.
# 인용수 리스트를 오름차순 정렬 후, citation[i]가 length-i보다 크거나 같으면 그 이후는 모두 크거나 같기 때문에 length-i를 h-index로 부여한다.


from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        citations.sort()

        for i in range(length):
            cur_h_index = length - i

            if citations[i] >= cur_h_index:
                return cur_h_index
        
        return 0