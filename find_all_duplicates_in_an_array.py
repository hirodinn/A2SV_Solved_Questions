class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for num in nums:
            # target index
            idx = abs(num) - 1
            
            # if the value at idx is negative, it's a duplicate
            if nums[idx] < 0:
                duplicates.append(abs(num))
            else:
                # mark as visited by making the value negative
                nums[idx] = -nums[idx]
        
        return duplicates
