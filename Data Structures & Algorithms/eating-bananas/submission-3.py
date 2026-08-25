class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            mid = (right - left) // 2 + left
            totaltime = 0
            for pile in piles:
                totaltime += math.ceil(pile/mid)
            if totaltime > h:
                left = mid + 1
            else:
                right = mid - 1
                res = min(res, mid)
        return res