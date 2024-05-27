def lalala(s1,s2):
    if len(s1)==len(s2):
        for i1,i2 in zip(s1,s2):
            if s1.count(i1) == s2.count(i2):
                return True
        else:
            return False
    else:
        return False
print(lalala('sssddd','pppooo'))
