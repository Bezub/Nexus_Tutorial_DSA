class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rt
        """
        outa = []
        county = 0
        for num in nums:
            for i in range(len(nums)):
                if num>nums[i]:
                    county += 1
            outa.append(county)
            county = 0
        return outa
tada = Solution()
print(tada)
