def subarray_sum(nums, target):
    # Initialize an empty dictionary to store cumulative sums and their indices
    sum_dict = {}
    # Initialize the cumulative sum
    cumulative_sum = 0
    
    # Loop through the array of numbers
    for index, num in enumerate(nums):
        # Add the current number to the cumulative sum
        cumulative_sum += num
        
        # Check if the cumulative sum is equal to the target
        if cumulative_sum == target:
            return [0, index]
        
        # Check if the difference between cumulative sum and target is in the dictionary
        diff = cumulative_sum - target
        if diff in sum_dict:
            return [sum_dict[diff] + 1, index]
        
        # Store the cumulative sum and its index in the dictionary
        sum_dict[cumulative_sum] = index
    
    # If no such subarray is found, return an empty list
    return []

# Example usage
nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))  # Output: [1, 3]
