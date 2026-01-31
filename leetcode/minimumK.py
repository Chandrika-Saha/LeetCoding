import math


def minimumK(nums):
    n = sum(nums) + 1
    l, r = 1, n
    res = 0
    while l <= r:
        i = (l + r) // 2
        count = 0
        for num in nums:
            count += (num + i - 1) // i

            if count > i * i:
                break

        if count <= i * i:
            res = i
            r = i - 1
        else:
            l = i + 1

    return res

print(minimumK([46278,53928,60070,7071,82822,91332,67650,87246,85002,71721,96262,56441,76148,59586,64252,33391,92290,62345,28236,44197,34849,5536,5742,6889,21347,45850,508,37986,85804,935,18404,8348,56066,89196,29120,79776,51972,73108,28964,59468,25278,44500]))


def longestSubsequence( nums):
    def isnonzero(sn):
        res = sn[0]
        for n in sn[1:]:
            res &= n
            print(f"anding {n} = {res}")
        return False if res == 0 else True

    sn = []
    for n in nums:
        if not sn or n > sn[-1]:
            sn.append(n)
    print(sn)

    while True:
        if isnonzero(sn):
            return len(sn)
        else:
            sn.pop(0)

    return 0

print(longestSubsequence([2, 3, 6]))