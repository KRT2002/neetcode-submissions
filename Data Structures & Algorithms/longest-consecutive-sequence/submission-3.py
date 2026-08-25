class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_arr = sorted(nums)
        lcs, index = 0, 0
        temp = 1

        while index < len(sorted_arr):
            if (index + 1 == len(sorted_arr)) or (sorted_arr[index] == sorted_arr[index+1]):
                index+=1
                continue
            if sorted_arr[index]+1 == sorted_arr[index+1]:
                temp += 1
            else:
                temp = 1
            
            index += 1
            lcs = max(lcs, temp)
        
        lcs = max(lcs, temp) if nums else lcs
        return lcs


