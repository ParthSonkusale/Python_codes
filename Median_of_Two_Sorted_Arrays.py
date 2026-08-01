class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = nums1 + nums2
        nums3.sort()
        n = len(nums3)
        half = n/2

        if n % 2 == 0:
            out = float((nums3[half] + nums3[half - 1]))/2
            return out
        else :
            out = float(nums3[half])  
            return out  