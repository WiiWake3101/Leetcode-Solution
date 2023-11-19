class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # Sort the list in ascending order
        nums.sort() 
       # Initialize the answer to 0
        ans = 0 
       # Initialize the count of unique numbers to 0
        up = 0 
       # Iterate over the list starting from the second number
        for i in range(1, len(nums)):
           # If the current number is different from the previous one
            if nums[i] != nums[i-1]: 
              # Increment the count of unique numbers   
              up += 1 
             # Add the count of unique numbers to the answer 
            ans += up 
        # Return the answer
        return ans  
