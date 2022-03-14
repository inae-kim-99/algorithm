# https: // leetcode.com/problems/decode-string/
# leetcode 394 : Decode String
# LEVEL : Medium

class Solution:
    def decodeString(self, s: str) -> str:
        start_bracket = s.find("[")
        if start_bracket != -1:
            stack = ["["]
            end_bracket = start_bracket + 1
            while len(stack) != 0:
                if s[end_bracket] == "[":
                    stack.append("[")
                elif s[end_bracket] == "]":
                    stack.pop()
                end_bracket += 1
            substr = s[start_bracket+1:end_bracket-1]

            for i in range(len(s)):
                if s[i].isdigit():
                    start_number = i
                    break

            return s[:start_number] + int(s[start_number:start_bracket]) * self.decodeString(substr) + self.decodeString(s[end_bracket:])
        else:
            return s
