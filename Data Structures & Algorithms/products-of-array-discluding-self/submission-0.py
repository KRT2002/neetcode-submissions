class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length_num = len(nums)
        prefix = [0]*length_num
        postfix = [0]*length_num
        result = []

        for index in range(length_num):
            if index == 0:
                prefix[index] = nums[index]
            else:
                prefix[index] = nums[index]*prefix[index-1]
            
            reverse_index = length_num-index-1
            if reverse_index == length_num-1:
                postfix[reverse_index] = nums[reverse_index]
            else:
                postfix[reverse_index] = nums[reverse_index] * postfix[reverse_index+1]
        
        for index in range(length_num):
            if index == 0:
                result.append(postfix[index+1])
            elif index == length_num-1:
                result.append(prefix[index-1])
            else:
                result.append(prefix[index-1]*postfix[index+1])
        
        return result

