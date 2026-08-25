class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        dict_s = {}
        dict_t = {}

        for index in range(len(s)):
            dict_s[s[index]] = 1 + dict_s.get(s[index], 0)
            dict_t[t[index]] = 1 + dict_t.get(t[index], 0)
        
        for key, value in dict_s.items():
            if key in dict_t and dict_t[key]==value:
                continue
            else:
                return False
        
        return True
        