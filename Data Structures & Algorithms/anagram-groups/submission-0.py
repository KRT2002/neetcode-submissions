class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = []
        for str_ in strs:
            a.append(["".join(sorted(str_)), str_])
        
        hashmap = defaultdict(list)

        for i in a:
            hashmap[i[0]].append(i[1])

        return list(hashmap.values())
