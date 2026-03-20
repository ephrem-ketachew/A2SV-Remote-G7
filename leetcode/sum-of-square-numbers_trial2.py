class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))
        while left <= right:
            num = left ** 2 + right ** 2
            if num == c:
                return True
            
            if num < c:
                left += 1
            else:
                right -= 1
                
        return False