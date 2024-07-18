class Solution:

    def encode(self, strs: list[str]) -> str:
        if strs == "":
            return ""
        else:
        
            st = ''
            for i in strs:
                st=st+ ' '
                for letter in i:
                    st = st + str(ord(letter))+" "
            st.strip()
            return st.strip()
        
            

    def decode(self, st: str) -> list[str]:
        if st == "":
            return ""
        else:
            st = st.strip()
            st = st.split('  ')
            st2 = "" 
            for i in st:
                i = i.split(' ')
                if st2 != '':
                    st2 = st2 + ' '
                for number in i:
                    st2 = st2 + chr(int(number))
            st2.strip()
            st2 = list(st2.split(' '))
            return st2
            
        


s = Solution()



res = s.encode(["ю"])
print(res)

print(s.decode(res))