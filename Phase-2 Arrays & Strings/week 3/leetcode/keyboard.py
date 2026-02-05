# 500. Keyboard Row
# Easy

# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

# Example 1:

# Input: words = ["Hello","Alaska","Dad","Peace"]

# Output: ["Alaska","Dad"]

# Explanation:

# Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.

# Example 2:

# Input: words = ["omk"]

# Output: []

# Example 3:

# Input: words = ["adsdf","sfd"]

# Output: ["adsdf","sfd"] 

# Constraints:

# 1 <= words.length <= 20
# 1 <= words[i].length <= 100
# words[i] consists of English letters (both lowercase and uppercase).

from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        
        char_map = dict()
        for ch in first_row:
            char_map[ch] = 0
        for ch in second_row:
            char_map[ch] = 1
        for ch in third_row:
            char_map[ch] = 2
        
        ans = []
        for word in words:
            lower_word = word.lower()
            group = char_map[lower_word[0]]
            if all(char_map[ch] == group for ch in lower_word):
                ans.append(word)
                
        return ans