"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Example 1:
Input: "ab-cd"
Output: "dc-ba"

Example 2:
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Note:
S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S doesn't contain \ or "
"""

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        let = [l for l in S if l.isalpha()]
        res = []
        for char in S:
            if char.isalpha():
                temp = let.pop()
                res.append(temp)
            else:
                res.append(char)
        return ''.join(res)
