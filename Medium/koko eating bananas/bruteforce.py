import math

def minEatingSpeed(piles, h):
    max_piles = max(piles)
    for rate in range(1, max_piles+1):
        if can_finish_eating(rate , piles, h):
            return rate
    return None

def can_finish_eating(rate, piles, h):
    hours_taken = 0
    for pile in piles:
        hours_taken += math.ceil(pile/rate)
    if hours_taken <= h:
        return True
    return False

print(minEatingSpeed([3, 6, 7, 11], 8))