class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        mp= {"G":"G", "()":"o", "(al)":"al"}
        result=""
        i = 0
        n = len(command)
        while i<n:
            if command[i]!="(":
                result += mp[command[i]]
                i +=1
            elif command[i] == "(" and command[i+1] == ")":
                res = command[i:i+2]
                result += mp[res]
                i +=2
            elif command[i] == "(" and command[i+3] == ")":
                res = command[i:i+4]
                result += mp[res]
                i +=4
        return result
sol = Solution()
print(sol)
