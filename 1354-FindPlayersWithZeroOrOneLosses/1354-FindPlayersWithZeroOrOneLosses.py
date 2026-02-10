# Last updated: 2/9/2026, 9:54:05 PM
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = Counter()
        losers = Counter()

        l_zero = []
        win = []

        for c in matches:
            winners[c[0]] +=  1
            losers[c[1]] += 1
        for key in winners:
            if key not in losers:
                l_zero.append(key)
        for key in losers:
            if losers[key] == 1:
                win.append(key)
        l_zero.sort()
        win.sort()
        return l_zero, win
