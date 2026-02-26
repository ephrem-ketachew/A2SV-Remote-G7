# 1002. Find Common Characters
# Easy

# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.

from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        for ch in set(words[0]):
            count = words[0].count(ch)
            for i in range(len(words)):
                count = min(count, words[i].count(ch))
            ans.extend([ch] * count)
            
        return ans