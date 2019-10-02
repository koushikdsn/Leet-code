"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        opt = ''
        l = len(s)
        max_len = 0
        part = [[0]*l for _ in range(l)]
        
        for i in range(l):
            part[i][i] = True
            max_len = 1
            opt = s[i]
            
        for i in range(l-1):
            if s[i] == s[i+1]:
                part[i][i+1] = True
                opt = s[i:i+2]
                max_len = 2
                
        for i in range(l):
            for j in range(0,i-1):
                if s[j] == s[i] and part[j+1][i-1]:
                    part[j][i] = True
                    if max_len < i-j+1:
                        opt = s[j:i+1]
                        max_len = i-j+1
        return opt