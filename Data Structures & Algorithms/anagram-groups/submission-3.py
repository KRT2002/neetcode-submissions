class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict_p = {}

        for str_ in strs:
            temp = [0] * 26
            for c in str_:
                index = ord(c)-ord("a")
                temp[index] += 1
            
            t_temp = tuple(temp)
            if t_temp in dict_p:
                dict_p[t_temp].append(str_)
            else:
                dict_p[t_temp] = [str_]
        
        return [value for value in dict_p.values()]