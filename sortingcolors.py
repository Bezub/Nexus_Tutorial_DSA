class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        res1 = []
        res2 = []
        res3 = []
        for i in range(n):
            if nums[i] == 0:
                res1.append(0)
            elif nums[i] == 1:
                res2.append(1)
            elif nums[i] == 2:
                res3.append(2)
        nums[:] = res1 + res2 + res3
