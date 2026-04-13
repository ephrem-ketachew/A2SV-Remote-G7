class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.queue = [0] * k
        self.front = 0
        self.rear = self.size - 1
        self.cur_size = 0
        
    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.front = (self.front - 1 + self.size) % self.size
            self.queue[self.front] = value
            self.cur_size += 1
            return True
        
        return False
        
    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
            self.cur_size += 1
            return True
        
        return False
        
    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.front = (self.front + 1) % self.size
            self.cur_size -= 1
            return True
        
        return False
        
    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.rear = (self.rear - 1 + self.size) % self.size
            self.cur_size -= 1
            return True
        
        return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.queue[self.front]
        return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.queue[self.rear]
        return -1

    def isEmpty(self) -> bool:
        return self.cur_size == 0

    def isFull(self) -> bool:
        return self.cur_size == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()