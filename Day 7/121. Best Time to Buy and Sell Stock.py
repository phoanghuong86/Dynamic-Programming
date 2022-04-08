class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val, max_val, max_diff = prices[0], prices[0], 0

        for elem in prices[1:]:
            if elem > max_val:
                # update max value
                max_val = elem

            if elem < min_val:
                # update min value and re-init max value
                min_val, max_val = elem, elem

            if max_val - min_val > max_diff:
                # check for max_diff
                max_diff = max_val - min_val

        return max_diff
