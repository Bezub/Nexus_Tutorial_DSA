class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        arr1 = []
        mine = 0
        times = len(piles)//3
        for _ in range(times):
            arr1.append(piles[-2:])
            piles.pop(-1)
            piles.pop(-1)
        for i in range(len(arr1)):
            mine += arr1[i][0]
        return mine
seee = Solution()
print(seee)
