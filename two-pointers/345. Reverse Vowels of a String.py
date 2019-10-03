"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        v = {'a','e','i','o','u','A','E','I','O','U'}
        l = 0
        r = len(s) - 1
        while l < r:
            if (s[l] in v) and (s[r] in v):
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            if s[l] not in v:
                l += 1
            if s[r] not in v:
                r -= 1
        return ''.join(s)