class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = min(time), max(time) * totalTrips
        while left < right:
            mid = (left + right) // 2
            total_trips = sum(min(mid // t, totalTrips) for t in time)
            if total_trips < totalTrips:
                left = mid + 1
            else:
                right = mid
        return left
