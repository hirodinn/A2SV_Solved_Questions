class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []

        mapping = dict()

        for num in nums:
            if num in mapping:
                mapping[num]+=1
            else:
                mapping[num] = 1
        
        for key in mapping:
            if mapping[key] > len(nums) / 3 : result.append(key)
        
        return result
