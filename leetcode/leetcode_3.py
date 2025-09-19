# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# leetcode 3 : Longest Substring Without Repeating Characters 
# LEVEL : Medium

# 풀이
# 초기값 left = 0, right = 확인하는 위치
# 문자열을 순서대로 확인하면서 이미 만난 문자열인 경우, left를 만난 문자열+1 위치로 옮긴 후 다시 다음 문자열을 확인한다.
# 확인할때마다 right-left+1로 길이를 업데이트한다.


class Solution:
    # Solution 1
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     length = len(s)

    #     if length <= 1:
    #         return length

    #     max_substring = 0
    #     visited = defaultdict(bool)
    #     visited[s[0]] = True
    #     start = 0

    #     for i in range(1, length):
    #         if visited[s[i]]:
    #             while visited[s[i]]:
    #                 visited[s[start]] = False
    #                 start += 1
            
    #         visited[s[i]] = True
    #         max_substring = max(max_substring, i - start + 1)

    #     return max_substring

    # Solution 2
    def lengthOfLongestSubstring(self, s: str) -> int:
        location = {}
        result = 0
        left = 0
        
        for right in range(len(s)):
            if s[right] in location and left <= location[s[right]]:
                left = location[s[right]] + 1
            
            location[s[right]] = right
            result = max(result, right-left+1)
            
        return result
            



