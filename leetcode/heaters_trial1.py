class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        min_radius = float('-inf')
        for house in houses:
            idx = bisect_right(heaters, house)
            pos1 = heaters[idx - 1] if idx - 1 >= 0 else float('inf')
            pos2 = heaters[idx] if idx < len(heaters) else float('inf')
            
            radius = min(abs(house - pos1), abs(house - pos2))
            min_radius = max(min_radius, radius)
            
        return min_radius