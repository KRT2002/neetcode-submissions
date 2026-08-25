class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}

        for index, num in enumerate(nums):
            if (target - num) in dict_:
                return [dict_[target-num], index]
            else:
                dict_[num] = index