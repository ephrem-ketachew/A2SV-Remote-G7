class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        n, m = len(houses), len(heaters)
        i = j = 0
        min_radius = float('-inf')
        for i in range(n):
            radius = abs(heaters[j] - houses[i])
            while j + 1 < m and radius >= abs(heaters[j + 1] - houses[i]):
                radius = abs(heaters[j + 1] - houses[i])
                j += 1
            
            min_radius = max(min_radius, radius)
            
        return min_radius