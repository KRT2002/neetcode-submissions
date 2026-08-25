class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left_pointer = 0
        result = 0

        for index in range(len(s)):
            while s[index] in charSet:
                charSet.remove(s[left_pointer])
                left_pointer += 1
            charSet.add(s[index])
            result = max(result, index - left_pointer + 1)
        
        return result