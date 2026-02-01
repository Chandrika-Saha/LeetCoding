def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k_res = r

        while l <= r:
            m = l + (r-l)//2
            k = 0
            for p in piles:
                k += math.ceil(p/m)
            if k > h:
                l = m + 1
            else:
                k_res = min(k_res, m)
                r = m - 1

        return k_res