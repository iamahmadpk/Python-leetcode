#Given an integer x, return true if x is a palindrome, and false otherwise.
#Example 1:
#Input: x = 121
#Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0): #check for -ve int
            return False
        i = x
        s = 0
        while(i > 0):
            d = i % 10 # to get the last digit of i using the modulo operator %
            s = s * 10 + d 
            i = i //  10 # updating "i", by performing integer division to remove the last digit
        if (x == s): 
            return True
        return False
sol = Solution()
result = sol.isPalindrome(121)
print(result)


#Time complexity: O(n), where n is the number of digits in the input x.
#Space complexity: O(1), indicating constant space usage


