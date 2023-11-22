class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # Initializing a deque with the starting index (0, 0)
        queue = deque([(0, 0)])
        # Initializing an empty list to store the result
        ans = []
        
        # While there are indices in the queue
        while queue:
            # Pop the leftmost index from the queue
            row, col = queue.popleft()
            # Append the corresponding element from nums to ans
            ans.append(nums[row][col])
            
            # If it's the first column and there's a row below
            if col == 0 and row + 1 < len(nums):
                # Append the index of the element below to the queue
                queue.append((row + 1, col))
                
            # If there's a column to the right
            if col + 1 < len(nums[row]):
                # Append the index of the element to the right to the queue
                queue.append((row, col + 1))
        
        # Return the result list
        return ans