class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        counter = Counter()
        left = 0
        count = 0
        k = -1
        for right in range(len(word)):
            if word[right] not in vowels:
                counter = Counter()
                left = right + 1
                k = - 1
            else:
                counter[word[right]] += 1
                
                if len(counter) == 5 and k == -1:
                    k = left
                    
                while len(counter) == 5 and counter[word[left]] > 1:
                    counter[word[left]] -= 1
                    left += 1
                    
                    
                if len(counter) == 5:
                    count += left - k + 1
                    
        return count