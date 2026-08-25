class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        if len(s)!=len(t):
            return False
        
        for i in s:
            if i in count_s:
                count_s[i]+=1
            else:
                count_s[i]=1
        
        for i in t:
            if i in count_t:
                count_t[i]+=1
            else:
                count_t[i]=1
        
        for key, value in count_s.items():
            if key in count_t:
                if count_t[key]!=value:
                    return False
            else:
                return False
        return True