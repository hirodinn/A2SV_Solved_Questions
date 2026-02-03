class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        toContinue = True
        i = 0
        while toContinue:
            toContinue = False
            for s in strs:
                if(i >= len(s) or s[i] != strs[0][i]):
                    break
            else:
                common += strs[0][i]
                toContinue = True
            i+=1
        return common
