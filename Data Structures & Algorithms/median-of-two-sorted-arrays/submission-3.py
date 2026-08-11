class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()

        n = len(nums3)

        if n % 2 == 0:
            left = n // 2 - 1
            right = n // 2
            return (nums3[left] + nums3[right]) / 2

        return nums3[n // 2]