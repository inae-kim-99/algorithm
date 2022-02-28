# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/
# leetcode : Replace Elements with Greatest Element on Right Side

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = -1
        for i in range(len(arr)-1, -1, -1):
            if arr[i] > max_num:
                temp = arr[i]
                arr[i] = max_num
                max_num = temp
            else:
                arr[i] = max_num
        return arr
