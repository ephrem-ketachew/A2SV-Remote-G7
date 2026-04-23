class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        def find_days(capacity: int) -> int:
            count_days = 0
            i = 0
            while i < n:
                curr = 0
                j = i
                while j < n and (curr + weights[j]) <= capacity:
                    curr += weights[j]
                    j += 1

                if j == i:
                    return days + 1
                else:
                    i = j

                count_days += 1

            return count_days
            

        low = 1
        high = sum(weights)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            count = find_days(mid)
            if count <= days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans


            