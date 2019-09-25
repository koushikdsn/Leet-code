"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def tracker(p='',l=0,r=0):
            if len(p) == 2*n:
                res.append(p)
                return
            if l < n:
                tracker(p+'(',l+1,r)
            if r < l:
                tracker(p+')',l,r+1)
        tracker()
        return res