class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spd = sorted([(pos, spd) for pos, spd in zip(position, speed)])
        n = len(pos_spd)
        count = 0
        prev_time = 0
        for i in range(n - 1, -1, -1):
            x, v = pos_spd[i]
            s = target - x
            t = s / v
            
            if t > prev_time:
                count += 1
                prev_time = t
                
        return count