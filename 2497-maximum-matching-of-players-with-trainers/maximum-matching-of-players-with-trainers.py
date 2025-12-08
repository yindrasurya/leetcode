class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        left = right = 0
        while left< len(players) and right < len(trainers):
            if trainers[right] >= players[left]:
                left += 1
                right += 1
            elif trainers[right] < players[left]:
                right += 1
            else:
                break
        return left  