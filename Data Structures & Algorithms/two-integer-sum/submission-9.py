class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, val in enumerate(nums):
            val2 = target - val
            if val2 in hash_map:
                return [hash_map[val2], index]
            hash_map[val] = index