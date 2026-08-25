class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initially sorted (ascending order) and then it is being rotated and thus created 
        # 2 independent sorted array
        # so if calculate mid then it must be in one sorted subarray
        # if arr[mid] > arr[left] then left sorted subarray their minimum is smallest value thta is arr[left]
        # if arr[mid] < arr[right] then right sorted subarray here we just have to shift right = mid - 1

        left, right = 0, len(nums) - 1
        res = nums[left]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                res = min(res, nums[mid])
                right = mid - 1
            else:
                res = min(res, nums[left])
                left = mid + 1
        return res