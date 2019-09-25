"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = {}
        for st in strs:
            tmp = ''.join(sorted(st))
            if tmp in grp:
                grp[tmp].append(st)
            else:
                grp[tmp] = [st]
        return [grp[i] for i in grp]