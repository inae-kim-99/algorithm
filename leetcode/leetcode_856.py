# https://leetcode.com/problems/score-of-parentheses/
# leetcode 856 : Score of Parentheses
# LEVEL : Medium

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack_count = 0
        start = 0
        score = 0
        for end in range(len(s)):
            if s[end] == '(':
                stack_count += 1
            elif stack_count > 0:
                stack_count -= 1
            if stack_count == 0:  # s[start:end+1]이 balanced parentheses string인 경우
                if end-start == 1:
                    score += 1
                else:
                    score += (2*self.scoreOfParentheses(s[start+1:end]))
                start = end+1

        return score
