"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard.
 
Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
 
Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""

class Solution:
    def findWords(self, words):
        line1 = set('qwertyuiop')
        line2 = set('asdfghjkl')
        line3 = set('zxcvbnm')
        result = []
        for word in words:
            w = set(word.lower())
            if w <= line1 or w <= line2 or w <= line3:
                result.append(word)
        return result