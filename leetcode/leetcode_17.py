# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# leetcode 17 : Letter Combinations of a Phone Number
# LEVEL : Medium

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        combinations = letters[digits[0]]
        for i in range(1, len(digits)):
            new_combinations = []
            for combination in combinations:
                for letter in letters[digits[i]]:
                    new_combinations.append(combination+letter)
            combinations = new_combinations

        return combinations
