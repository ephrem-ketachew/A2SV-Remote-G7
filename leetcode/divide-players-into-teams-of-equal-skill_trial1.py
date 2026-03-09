class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right = 0, len(skill) - 1
        total = 0
        s = skill[0] + skill[-1]
        while left < right:
            if skill[left] + skill[right] != s:
                return -1
            total += skill[left] * skill[right]
            left += 1
            right -= 1

        return total
