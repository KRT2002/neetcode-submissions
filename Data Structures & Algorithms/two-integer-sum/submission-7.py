class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = [(num, i) for i, num in enumerate(nums)]
        a.sort()
        i, j = 0, len(nums)-1
        while i<j:
            current = a[i][0] + a[j][0]
            if current == target:
                return [min(a[i][1], a[j][1]), max(a[i][1], a[j][1])]
            elif current > target:
                j -= 1
            else:
                i += 1