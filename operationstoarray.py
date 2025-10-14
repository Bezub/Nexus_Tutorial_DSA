class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        n = len(nums)
        while i<n-1:
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
            i += 1
        result = []
        zeros = 0
        for x in nums:
            if x != 0:
                result.append(x)
            else:
                zeros +=1
        result.extend([0]*zeros)
        return result

sol = Solution()
print(sol)
