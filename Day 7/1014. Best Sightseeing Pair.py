class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_seen, max_score = values[0], 0
        for x in values[1:]:
            max_seen -= 1
            current, max_seen = x + max_seen, max(x, max_seen)
            max_score = max(current, max_score)
        return max_score    
