# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# leetcode 17 : Letter Combinations of a Phone Number
# level : Medium

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        buttons = {"2": ['a', 'b', 'c'],
                   "3": ['d', 'e', 'f'],
                   "4": ['g', 'h', 'i'],
                   "5": ['j', 'k', 'l'],
                   "6": ['m', 'n', 'o'],
                   "7": ['p', 'q', 'r', 's'],
                   "8": ['t', 'u', 'v'],
                   "9": ['w', 'x', 'y', 'z']}

        combinations = [""]
        for digit in digits:
            new_combinations = []
            for letters in combinations:
                for new_letter in buttons[digit]:
                    new_combinations.append(letters+new_letter)
            combinations = new_combinations

        return combinations
