class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if s is None: 
            return ""
        if numRows < 2 or len(s) < numRows:
            return s

        result = ""
        step = 2 * numRows - 2
        for i in range(0, numRows):
            for j in range(i, len(s), step):
                result += s[j]
                if i != 0 and i != numRows - 1 and (j + step - 2 * i) < len(s):
                    result += s[j + step - 2 * i]
        return result


# [00]P                               [06]I                               [12]N
# [01]A                   [05]L       [07]s                   [11]I       [13]G
# [02]Y       [04]A                   [08]H       [10]R
# [03]P                               [09]I
