class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        
        currMin, currMax = 1, 1
        
        for n in nums:
            temp = currMax * n # to avoid update of current currMax
            currMax = max(n*currMax, n*currMin, n)
            currMin = min(temp, n*currMin, n)
            res = max(res, currMax,currMin)
           
        return res
