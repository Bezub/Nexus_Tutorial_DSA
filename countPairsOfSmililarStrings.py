class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        my_list = [set(word) for word in words]
        count = 0
        for j in range(len(my_list)):
            for i in range(j+1,len(my_list)):
                if my_list[j] == my_list[i]:
                    count += 1
        return count
sol = Solution()
print(sol)
