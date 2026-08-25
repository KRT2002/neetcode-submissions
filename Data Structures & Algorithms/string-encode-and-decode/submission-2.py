class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for str_ in strs:
            res += f"{len(str_)}#{str_}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        total_len = len(s)
        i = 0
        while i < total_len:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
    