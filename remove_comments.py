class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        block_comment_occured = False
        result = []
        myLine = ""
        for line in source:
            if not block_comment_occured : myLine = ""
            i = 0
            while i < len(line):
                if (not block_comment_occured) and i != len(line) - 1 and line[i:i+2] == "//":
                    break
                if not block_comment_occured and i != len(line) - 1 and line[i:i+2] == "/*":
                    block_comment_occured = True
                    i+=1
                elif block_comment_occured and (i != len(line) - 1 and line[i:i+2] == "*/"):
                    block_comment_occured = False
                    i+=2
                    continue
                if not block_comment_occured : myLine += line[i]
                i+=1
            if myLine and not block_comment_occured : result.append(myLine)                
        return result
            

        
