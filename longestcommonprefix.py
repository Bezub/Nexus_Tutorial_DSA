class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        m = len(min(strs, key=len))
        n = len(strs)
        result = ""
        for i in range(m):
            chrs = strs[0][i]
            for j in range(1,len(strs)):
                if chrs != strs[j][i]:
                    return result
            result += chrs
        return result
        
        
        return result
