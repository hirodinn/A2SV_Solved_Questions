class Solution:    
    def findUnion(self, a, b):
        result = list(set(a+b))
        # while (i < len(a) or i < len(b)) and (a not in result or b not in result):
        #     if i < len(a) and a[i] not in result:
        #         result.append(a[i])
        #     if i < len(b) and b[i] not in result:
        #         result.append(b[i])
            
        #     i+=1
        
        return result
