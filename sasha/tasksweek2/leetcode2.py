class Solution(object):
    def reverseWords(self,s):
        """
        :type s: str
        :rtype: str
        """
        "remove spaces at the beginning and end of the string"
        s = s.strip()
        "split the line into words"
        s = s.split(' ')
        result = []
        "remove unnecessary spaces"
        for i in s:
            if i != '':
                result.append(i)
                continue            
        "write string of the words in reverse order"    
        result = list(reversed(result))
        return ' '.join(result)
        
         
solution = Solution()


print(solution.reverseWords(" the sky is blue" ))
print(solution.reverseWords("  hello world  "))
print(solution.reverseWords("a good   example"))