class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        obj = {}

        # Count frequencies
        for num in nums:
            if num in obj:
                obj[num] += 1
            else:
                obj[num] = 1

        # Sort by frequency (highest first)
        obj = dict(sorted(obj.items(), key=lambda x: x[1], reverse=True))

        # Return first k keys
        arr = list(obj.keys())[:k]

        return arr