# https://leetcode.com/problems/partition-labels/
# leetcode 763 : Partition Labels
# LEVEL : Medium

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = [0]

        for end in range(1, len(s)):
            start = sum(result)
            if not self.include(s[start:end], s[end:]):
                result.append(end-start)

        result.append(len(s)-sum(result))

        return result[1:]

    def include(self, s1, s2) -> bool:
        for s in s1:
            if s in s2:
                return True
        return False


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []

        map = {}
        for i in range(len(s)):
            map[s[i]] = i

        start = 0
        max_idx = 0
        for i in range(len(s)):
            max_idx = max(max_idx, map[s[i]])
            if max_idx == i:
                res.append(i-start)
                start = i+1

        return res
