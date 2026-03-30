class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        del_count = 0
        can_be_palindrome = True
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                del_count += 1
                if del_count > 1:
                    can_be_palindrome = False
                    break
                
                right -= 1
                
        if can_be_palindrome:
            return True
        
        left, right = 0, len(s) - 1
        del_count = 0
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                del_count += 1
                if del_count > 1:
                    return False
                left += 1
                
        return True