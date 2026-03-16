class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_recolor = win_recolor = blocks[:k].count('W')
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                win_recolor += 1
            if blocks[i - k] == 'W':
                win_recolor -= 1
                
            min_recolor = min(min_recolor, win_recolor)
            
        return min_recolor