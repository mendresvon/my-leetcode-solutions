class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {} # {val: idx}

        for idx, val in enumerate(nums):
            dif = target - val
            if dif in seen_map:
                return [seen_map[dif], idx]
            seen_map[val] = idx