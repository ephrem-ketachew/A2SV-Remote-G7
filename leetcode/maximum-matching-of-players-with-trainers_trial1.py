class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        n, m = len(players), len(trainers)
        p = t = 0
        while p < n and t < m:
            if players[p] <= trainers[t]:
                p += 1
                t += 1
            else:
                t += 1

        return p
