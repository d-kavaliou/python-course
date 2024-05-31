def detect_pattern(s1, s2):
    if len(s1) == len(s2):
        def dict_maker(s): #создает из списка словарь, где каждому символу соответствует число
            s_unique = []
            s_dict = {}
            val = 1
            for key in s:
                if key not in s_unique:
                    s_dict.update({key: val})
                    val += 1
            return s_dict
        dict_s1 = dict_maker(s1)
        dict_s2 = dict_maker(s2)
        def translator(s, d): # "переводит" каждый символ в числовое значение из словаря и делает строку
            translation = []
            for el in s:
                translation.append(d[el])
            return translator
        s1_translation = translator(s1, dict_s1)
        s2_translation = translator(s2, dict_s2)
        return s1_translation == s2_translation
    else:
        return False
    

s1 = 'aaa'
s2 = 'zzz'
s3 = 'qwerqww'
s4 = 'asdfass'
s5 = ''
s6 = ''
s7 = 'rjrjfh'
s8 = 'djdhd'
print(detect_pattern(s1,s2))
print(detect_pattern(s3,s4))
print(detect_pattern(s5,s6))
print(detect_pattern(s7,s8))

