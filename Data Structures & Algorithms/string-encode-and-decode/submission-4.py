class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for char in strs:
            res += f"{len(char)}!{char}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        total_len = len(s)
        i = 0
        while i < total_len:
            temp=0
            while s[i+temp]!="!":
                temp+=1
            sub_len = int(s[i:i+temp])
            i += temp + 1
            sub_str = s[i:i+sub_len]
            res.append(sub_str)
            i += sub_len
        return res