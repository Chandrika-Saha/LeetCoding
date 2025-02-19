class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        if l1 == 1 and l2 == 1:
            return (nums1[0] + nums2[0]) / 2
        lt = l1 + l2
        hl = lt // 2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1) - 1

        while True:
            m = l + (r - l) // 2
            mo = hl - m - 2

            num1_l = nums1[m] if m >= 0 else float('-inf')
            num1_r = nums1[m + 1] if (m+1) < len(nums1) else float('inf')
            num2_l = nums2[mo] if mo >= 0 else float('-inf')
            num2_r = nums2[mo + 1] if (mo + 1) < len(nums2) else float('inf')

            # We found the correct partition 
            if num1_l <= num2_r and num2_l <= num1_r:
                if lt % 2:
                    return min(num1_r, num2_r)
                return (max(num1_l, num2_l) + min(num1_r, num2_r)) / 2

            elif num1_l > num2_r:
                r = m - 1
            else:
                l = m + 1

            


                