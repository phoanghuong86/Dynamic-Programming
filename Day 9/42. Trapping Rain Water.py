class Solution:
    def trap(self, height: List[int]) -> int:
        # Brute Force
        # For each spot
        # water = min(left_max, right_max) - height[i]
        # O(n^2)
        # Bottle Neck: finding the left_max and right_max
        
        ############################## Optimization ##############################
        # Dynamic Programming -> Memorization
        # First iteration -> Store left_max for each spot
        spots = []
        left_max, right_max = 0, 0
        result = 0
        for index, value in enumerate(height):
            # Update left_max when the left bar increased -> which will result in a higher potential for net water pot
            if value > left_max:
                left_max = value
            spots.append(left_max)
        # Second iteration -> Store right_max for each spot
        for index in range(len(height) - 1, 0, -1):
            # Update right_max when the right bar increased -> which will result in a higher potential for net water pot
            if height[index] > right_max:
                right_max = height[index]
            left_max = spots[index]
            # Mathmatical pattern for water got trapped
            result += min(left_max, right_max) - height[index]
        return result
