class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = deque()
        self.hash_map = Counter()
        

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        self.hash_map[num] += 1

        if len(self.queue) < self.k:
            return False

        if len(self.queue) > self.k:
            popped_num = self.queue.popleft()
            self.hash_map[popped_num] -= 1
            if self.hash_map[popped_num] == 0:
                del self.hash_map[popped_num]

        return len(self.hash_map) == 1 and self.value in self.hash_map


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)