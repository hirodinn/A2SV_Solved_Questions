class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        l = list(chars)
        result = 0
        for word in words:
            lst = list(l)
            for w in word:
                if w in lst:
                    lst.remove(w)
                else :
                    break
            else:
                result += len(word)
        
        return result
