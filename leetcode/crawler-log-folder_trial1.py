class Solution:
    def minOperations(self, logs: List[str]) -> int:
        deep_count = 0
        for ch in logs:
            if ch == './':
                continue
            if ch == '../':
                deep_count = max(0, deep_count - 1)
            else:
                deep_count += 1
                
        return deep_count