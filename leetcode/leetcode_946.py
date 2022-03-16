# https://leetcode.com/problems/validate-stack-sequences/
# leetcode 946 : Validate Stack Sequences
# LEVEL : Medium

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for push in pushed:
            stack.append(push)
            while len(stack) and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return len(stack) == 0
