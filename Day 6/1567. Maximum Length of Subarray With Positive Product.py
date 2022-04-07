class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        @cache
        def max_len_starting_with(index, positive=True):
            if index >= len(nums) or nums[index] == 0:
                return 0
            
            length = 0
            if (nums[index] > 0) is positive:
                # the sign for current element is correct, so simply take the current element, plus the next longest possible positive subarray
                length = 1 + max_len_starting_with(index + 1, True)
            else:
                # the sign for current element is incorrect, so we need to flip the sign by taking a negative subarray
                if next_neg := max_len_starting_with(index + 1, False):
                    length = 1 + next_neg
            
            return length

        return max(max_len_starting_with(i) for i in range(len(nums)))
