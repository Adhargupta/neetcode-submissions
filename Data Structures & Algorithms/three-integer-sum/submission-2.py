class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                third = -(nums[i] + nums[j])

                if third in nums[j + 1:]:
                    triplet = sorted([nums[i], nums[j], third])

                    if triplet not in arr:
                        arr.append(triplet)

        return arr