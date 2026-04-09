class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # counter = Counter()
        # left = 0
        # min_heap = []
        # max_heap = []
        # max_len = 0
        # for right, num in enumerate(nums):
        #     counter[num] += 1
        #     heapq.heappush(min_heap, num)
        #     heapq.heappush(max_heap, -num)      

        #     while max_heap and min_heap and (-max_heap[0] - min_heap[0] > limit):
        #         num = nums[left]
        #         counter[num] -= 1
        #         if counter[num] == 0:
        #             del counter[num]

        #         while max_heap and counter[-max_heap[0]] == 0:
        #             heapq.heappop(max_heap)

        #         while min_heap and counter[min_heap[0]] == 0:
        #             heapq.heappop(min_heap)

        #         left += 1
                
        #     max_len = max(max_len, right - left + 1)

        # return max_len
        
        min_queue = deque()
        max_queue = deque()
        max_len = 0
        left = 0
        for right, num in enumerate(nums):
            while min_queue and num < nums[min_queue[-1]]:
                min_queue.pop()
            min_queue.append(right)
            
            while max_queue and num > nums[max_queue[-1]]:
                max_queue.pop()
            max_queue.append(right)
            
            while nums[max_queue[0]] - nums[min_queue[0]] > limit:
                if left == max_queue[0]:
                    max_queue.popleft()
                if left == min_queue[0]:
                    min_queue.popleft()
                left += 1
                
            max_len = max(max_len, right - left + 1)
             
        return max_len