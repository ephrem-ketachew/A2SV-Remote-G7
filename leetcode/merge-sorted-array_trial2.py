class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n + m - 1, n - 1, - 1):
            nums1[i] = nums1[i - n]

        first, second = n, 0
        i = 0
        while first - n < m and second < n:
            if nums1[first] <= nums2[second]:
                nums1[i] = nums1[first]
                first += 1
            else:
                nums1[i] = nums2[second]
                second += 1
            i += 1

        while first - n < m:
            nums1[i] = nums1[first]
            first += 1
            i += 1

        while second < n:
            nums1[i] = nums2[second]
            second += 1
            i += 1
