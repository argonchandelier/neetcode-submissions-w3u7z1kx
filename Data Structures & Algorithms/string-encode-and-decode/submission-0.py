class Solution:

    def encode(self, strs: List[str]) -> str:
        full_str = ""
        for s in strs:
            for char in s:
                if char == "/":
                    full_str += "//"
                else:
                    full_str += char
            full_str += "/n"
        full_str += ("/e" + str(len(strs)))
        return full_str

    def decode(self, s: str) -> List[str]:
        if s == "/e0":
            return []

        len_fs = len(s)
        str_len = ""
        neg_count = len_fs - 1
        while(True):
            if s[neg_count] == "e":
                str_len = int(str_len)
                break
            str_len = s[neg_count] + str_len
            neg_count -= 1

        strs = [""] * str_len
        count = 0
        str_i = 0
        str_n = ""
        while(True):
            char = s[count]
            if char == "/":
                char2 = s[count+1]
                if char2 == "/":
                    str_n += "/"
                elif char2 == "n":
                    strs[str_i] = str_n
                    str_n = ""
                    str_i += 1
                elif char2 == "e":
                    break
                count += 2
            else:
                str_n += char
                count += 1
        
        return strs





