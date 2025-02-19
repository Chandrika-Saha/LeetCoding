class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        first, second = 0, 0
        merged = []
        while first < len(nums1) and second < len(nums2):
            if nums1[first] < nums2[second]:
                merged.append(nums1[first])
                first += 1
            else:
                merged.append(nums2[second])
                second += 1
        if first < len(nums1):
            merged.extend(nums1[first:])
        if second < len(nums2):
            merged.extend(nums2[second:])
        
        print(merged)

        n = len(merged)
        if n % 2 == 0:
            n = n - 1
            return (merged[n // 2] + merged[(n // 2) + 1]) / 2
        else:
            return merged[((n-1)//2)]
       

        return 0.0
                