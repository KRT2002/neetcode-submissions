class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We are performing sorting which shuffles indices order as well.
        # So while sorting we have to preserve the original index order as well
        # Thus new list of tuple creating -> List[(value, index)]
        # The reason we are using tuple inside list because in order to ensure immutability.
        # The reason we are using sort over sorted because first of all we are dealing with list itearble and also we don't want to create one more copy of list
        # sorted also works but it create copy of sorted list 

        a = []
        for index, elem in enumerate(nums):
            a.append((elem, index))
        
        a.sort()
        i, j = 0, len(nums)-1   # Counter or 2-pointer
        while i < j:    # ensures no uncessary checks
            if a[i][0] + a[j][0] == target:
                return [min(a[i][1], a[j][1]), max(a[i][1], a[j][1])]
            elif a[i][0] + a[j][0] > target:
                j -= 1
            else:
                i += 1