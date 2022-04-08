class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        p = 0
        prev = nums[0]
        for i in range(1 , len(nums)):
            if nums[i] < nums[i-1] :
                p += nums[i-1] - prev
                prev = nums[i]
            elif i == len(nums)-1:
                p += nums[i] - prev
        return p
