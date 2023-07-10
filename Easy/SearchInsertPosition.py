from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
    	#using binary search as array is sorted and we have to do it with O(nlogn)
    	beg = 0
    	end = len(nums)-1
    	while end >= beg:
    		mid = (beg + end) // 2
    		if target == nums[mid] : return mid
    		#if target is greater than mid element then move to right
    		elif target > nums[mid]: 
    			beg = mid + 1
    		#if target is less that mid element then move to left
    		else:
    			end = mid -1
    	#if not found return beg
    	return beg
sol = Solution()
nums = [1,2,4,9,11]
target = 10
result = sol.searchInsert(nums,target)
print(result)

