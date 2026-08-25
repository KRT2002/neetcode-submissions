class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_ = {}
        for n in nums:
            dict_[n] = 1 + dict_.get(n, 0)
            if dict_[n]>=2:
                return True
        return False