# https: // leetcode.com/problems/boats-to-save-people/
# leetcode 881 : Boats to Save People
# LEVEL : Medium

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        light = 0
        heavy = len(people)-1
        boats = 0

        while light < heavy:
            if people[light] + people[heavy] <= limit:
                light += 1
                heavy -= 1
            else:
                heavy -= 1
            boats += 1

        if light != heavy:
            return boats
        else:
            return boats + 1
