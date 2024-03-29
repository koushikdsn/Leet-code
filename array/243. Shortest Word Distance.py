"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Input: word1 = �coding�, word2 = �practice�
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        l = len(words)
        i1, i2 = l, l
        res = l
        
        for i in range(l):
            if words[i] == word1:
                i1 = i
                res = min(res, abs(i1-i2))
            elif words[i] == word2:
                i2 = i
                res = min(res, abs(i1-i2))
        return res