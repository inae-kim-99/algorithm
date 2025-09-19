# https://leetcode.com/problems/longest-repeating-character-replacement/
# leetcode 424 : Longest Repeating Character Replacement
# LEVEL : Medium

# 풀이
# 초기값 left = 0, right = 확인하는 문자열 위치
# 문자열을 하나씩 확인하면서 지금까지의 가장 많은 문자열의 빈도수를 f라 할 때,
# (right - left + 1) - f 가 k보다 크면 right를 오른쪽으로 하나 옯긴다.


from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0

        max_frequency = 0
        frequency = defaultdict(int)

        left = 0
        for right in range(len(s)):
            frequency[s[right]] += 1
            max_frequency = max(frequency[s[right]], max_frequency)

            if (right - left + 1) - max_frequency > k:
                frequency[s[left]] -= 1
                left += 1

            max_length = max(right - left + 1, max_length)

        return max_length
