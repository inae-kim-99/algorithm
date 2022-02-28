# https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/
# leetcode : Valid Mountain Array

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        top = -1
        for i in range(len(arr)-1):
            if arr[i] >= arr[i+1]:
                top = i
                break
        if top == 0:
            return False
        for i in range(top, len(arr)-1):
            if arr[i] <= arr[i+1]:
                return False
        return True
