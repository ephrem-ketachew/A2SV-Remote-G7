class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(float('-inf'))
        for i, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                right_idx = stack.pop()
                rect_height = heights[right_idx]
                
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                    
                area = rect_height * width
                max_area = max(max_area, area)
                
            stack.append(i)
            
        return max_area