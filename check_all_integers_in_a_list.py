class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        i = 0
        ranges.sort()
        while left <= right and i < len(ranges):
            if ranges[i][0] <= left <= ranges[i][1] :
                left+=1
            else:
                i+=1
        return True if left > right else False
        
