#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if #the input string is valid.
#An input string is valid if:
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type. 
#Example 1:
#Input: s = "()"
#Output: true

#Approach:
#Initialize a Stack
#Process each bracket one at a time. if we encounter a opening bracket push it into the stack and if closing bracket then check its opening bracket available at top of stack if yes then pop it from stack if not the return Flase.
#in the end if we are left with a non-empty stack then it is invalid return False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(", "]":"[","}":"{"} #map
        if(len(s)%2!=0): return False #check if lenght of string is an odd number, return false at O(1) time 
        else:
            for c in s:	
                if c in closeToOpen:
                    if stack and stack[-1] == closeToOpen[c]: #if Stack in non-empty and top of stack is same as required in closedToOpen
                        stack.pop()	#delete the opening bracket from stack
                    else:
                        return False
                else: 
                    stack.append(c)	#if encounters opening bracket then append in stack
            return True if not stack else False
            
#Time Complexity:	O(n), beacuse we will iterate the whole string only one time ..n is the nubmer of elements in string
#Space Complexity:	(n), stack will take extra space n is the number of characters appended to stack
