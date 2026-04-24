class MyCalendar:

    def __init__(self):
        self.bookings = [(-2, -1)]
        

    def book(self, startTime: int, endTime: int) -> bool:        
        i = 0
        while i < len(self.bookings) and self.bookings[i][0] < startTime:
            i += 1
            
        if i == len(self.bookings):
            if startTime >= self.bookings[-1][1]:
                self.bookings.append((startTime, endTime))
                return True
            return False
        
        self.bookings.insert(i, (startTime, endTime))
        if startTime >= self.bookings[i - 1][1] and endTime <= self.bookings[i + 1][0]:
            return True
        
        self.bookings.pop(i)
        return False
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)