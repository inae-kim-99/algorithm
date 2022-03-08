# https://leetcode.com/problems/generate-parentheses/submissions/
# leetcode 22 : Generate Parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        p = {"(": 1}
        for i in range(2*n-1, 0, -1):
            new_p = {}
            for key, value in p.items():
                if value == 0:
                    new_p[key+"("] = value+1
                elif i-value > 0:
                    new_p[key+"("] = value+1
                    new_p[key+")"] = value-1
                else:
                    new_p[key+")"] = value-1
            p = new_p

        return new_p.keys()
