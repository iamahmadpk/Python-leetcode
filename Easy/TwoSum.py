#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.
#Example 1:=
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#map will be like this
	#thisdict = {
  #2: 0,
  #7: 1,
  #11: 2,
  #15: 3
#}

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    	lookUp = {}	# Initialize an empty dictionary
    	for i in range(len(nums)):
    		sub = target - nums[i]	# Calculate the difference
    		if sub in lookUp:	# Check if the difference exists in the dictionary
    			return[i,lookUp[sub]]	# Return the indices of the two numbers
    		lookUp[nums[i]] = i	# Add the current number and its index to the dictionary

twosum = Solution()
nums = [2,7,11,15]
result = twosum.twoSum(nums,9)
print("indices of two sum is ", result)

#Time Complexity = O(n). We traverse the list containing n elements only once. 
#Space Complexity = O(n). The extra space required depends on the number of items stored in the hash table, which stores at most n elements.
#LookUp Time Complexity = Each lookup in the table costs only O(1) time.






