class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * (2 * n)
        stack = []
        double = nums * 2
        for i, num in enumerate(double):
            while stack and num > double[stack[-1]]:
                idx = stack.pop()
                ans[idx] = num
            stack.append(i)
            
        return ans[:n]