"""
case 1 : nums = [2,7,11,15], target = 9
case 2 : nums = [3,2,4], target = 6
case 3 : nums = [3,3], target = 6
"""

def twoSum(nums, target):
    # Dictionary to store numbers we've seen and their indices
    seen = {}
    
    # Iterate through the list
    for i, num in enumerate(nums):
        diff = target - num  # The number we need to find to make the sum equal to target
        
        # Check if the required number is already in the dictionary
        if diff in seen:
            return [seen[diff], i]  # Return indices of the two numbers
        
        # Store the current number and its index in the dictionary
        seen[num] = i
