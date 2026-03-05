class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        cdict = {}
        mlen = 0
        mfrq = 0

        for r in range(len(s)):
            
            cdict[s[r]] = cdict.get(s[r], 0) + 1

            mfrq = max(mfrq, cdict[s[r]])

            while (r - l + 1) - mfrq > k:
                cdict[s[l]] -= 1
                l += 1

            mlen = max(mlen, (r-l+1))

        return mlen

        