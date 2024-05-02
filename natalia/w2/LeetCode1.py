# 151. Reverse Words in a String

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def f(el):
            return el.strip()
    
        f(s)
        old_s = s.split()
        new_s = map(f,old_s[::-1])
        return ' '.join(new_s)