class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        occurence = dict()
        for path in paths:
            l = path.split()
            for i in range(1, len(l)):
                key = l[i][l[i].index("(") + 1: len(l[i]) - 1]
                if key in occurence:
                    occurence[key].append(l[0]+"/" + l[i][:l[i].index("(")])
                else:
                    occurence[key] = [f"{l[0]}/{l[i][:l[i].index("(")]}"]
        result = []
        for key in occurence:
            if len(occurence[key]) > 1 : result.append(occurence[key])
        return result


        
