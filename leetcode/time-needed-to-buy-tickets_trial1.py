class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        queue = deque(tickets)
        while True:
            for _ in range(k):
                ticket_left = queue.popleft()
                if ticket_left > 0:
                    ticket_left -= 1
                    count += 1
                queue.append(ticket_left)
                    
            ticket_k = queue.popleft()
            ticket_k -= 1
            count += 1
            if ticket_k == 0:
                return count
            
            queue.append(ticket_k)
            for _ in range(len(tickets) - k - 1):
                ticket_left = queue.popleft()
                if ticket_left > 0:
                    ticket_left -= 1
                    count += 1
                queue.append(ticket_left)

                    