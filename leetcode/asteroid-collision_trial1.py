class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if (not stack) or (asteroid > 0) or (stack[-1] < 0):
                stack.append(asteroid)
                continue
            
            while stack and (stack[-1] > 0) and (abs(asteroid) > stack[-1]):
                stack.pop()
                
            if stack and stack[-1] == abs(asteroid):
                stack.pop()
            elif not stack or stack[-1] < 0:
                stack.append(asteroid)
                
        return stack