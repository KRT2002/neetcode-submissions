class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        sub = set()

        while r < len(s):
            if s[r] not in sub:
                sub.add(s[r])
                res = max(res, r - l + 1)
                r += 1
            else:
                while l < r and s[r] in sub:
                    sub.remove(s[l])
                    l += 1
        return res