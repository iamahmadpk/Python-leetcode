#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".
#Example 1:
#Input: strs = ["flower","flow","flight"]
#Output: "fl"
#Sol#1
#Horizontal Scaling

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs) == ''): #check for empty string
            return ''
        if(len(strs) == 1): #if string len is 1
            return strs[0]
        prefix = ''	# let prefix is an empty string
        #finds the shortest string in the list and assigns it to prefix
        #O(m*n)
        for i in strs:
            if(len(i) < len(prefix) or prefix == ''):
                prefix = i
        #we need to make sure that  occurence of longest prefix found mux be equal to number of element in an array
        need = len(strs)
        count = 0
        result = ''
        #O(n)
        while(need != count):
            count = 0
            for i in strs:
            #compares whether the shortest string is present in other element 
                if(prefix == i[ : len(prefix)]):
                    count +=1
            result = prefix
            prefix = prefix[: -1]	# extracting/decreasing the one char from string
        if(need == count):
            return result
        else:
            return ''
#Time Complexity: O(m * n^2) ,m is the length of the array and n is the length of the longest string
#Space Complexity: O(m * n)

#Code to for Horizontal scaling 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #check for empty string
        if not strs:
            return ""

        prefix = strs[0]  # Initialize the prefix as the first string in the array

        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:	#Searches for the occurrence of the prefix	
                prefix = prefix[:-1]  # Remove the last character from the prefix

                if not prefix:  # If prefix becomes empty, there is no common prefix
                    return ""

        return prefix
        
#Time Complexity: O(m*n), m is the length of the array and n is the length of the longest string
#Space Complexity: O(1)
