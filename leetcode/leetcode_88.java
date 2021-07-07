// https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/
// Problem : Merge Sorted Array

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {

        int[] temp = nums1.clone();
        int count = 0, idx1 = 0, idx2 = 0;

        while (idx1 < m && idx2 < n) {
            if (temp[idx1] < nums2[idx2]) {
                nums1[count++] = temp[idx1++];
            } else {
                nums1[count++] = nums2[idx2++];
            }
        }

        if (idx1 < m) {
            while (idx1 < m)
                nums1[count++] = temp[idx1++];
        } else if (idx2 < n) {
            while (idx2 < n)
                nums1[count++] = nums2[idx2++];
        }
    }
}