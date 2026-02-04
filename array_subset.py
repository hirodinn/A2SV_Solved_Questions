#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        a.sort()
        b.sort()
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if(a[i] != b[j]): i+=1
            else :
                i+=1
                j+=1
        return j == len(b)
    
    
    
