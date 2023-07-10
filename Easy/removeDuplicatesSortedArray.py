from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #we will use two pointer to once to traverse the array the one is to keep the record of where we have to place the next unique elelemt
        left =1
        for right in range(1, len(nums)):
        	#compare if previous element is not same as the current means there is new unique element 
        	if nums[right-1] != nums[right]:
        		nums[left] = nums[right]
        		left +=1
        return left
        
sol = Solution()
nums = [0,0,1,1,2,2,3,3,4,4,5,5,9,9,9]
result = sol.removeDuplicates(nums)
print(result)

#Time complexity O(n)
#Space Complexity O(1)

