
def lalala(s1,s2):
    if len(s1)==len(s2):
        s1_s2 = dict(zip(s1,s2))
        result = []
        for i1 in s1:
            result.append(s1_s2.get(i1))
        if result == list(s2):
            return True
        else:
            return False
    else:
        return False

print(lalala("xyzxyzxyz","cbacbacba"))
print(lalala("abcdefghijk","lmnopqrstuv"))
print(lalala("asasasasas","xxxxxyyyyy"))
print(lalala("aaasssiiii","gggdddfffh"))
print(lalala("aba","xyz"))
print(lalala("a","x"))
print(lalala("aba","xyz"))
print(lalala("hh","g"))