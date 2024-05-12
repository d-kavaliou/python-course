"""Напишите алгоритм определения счастливого числа .
Счастливое число — это число, определяемое следующим процессом:
Начиная с любого положительного целого числа, 
замените число суммой квадратов его цифр.
Повторяйте процесс до тех пор, пока число не станет равным 1 
(где оно и останется),
или пока он не будет повторяться бесконечно в цикле
, который не включает 1.
Счастливыми являются те числа, для которых этот
процесс заканчивается на 1 .
Возвращает, true если n это счастливое число, а false если нет"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def kv(n):
            summ = 0
            for i in str(n):
                summ += int(i)*int(i)
            return summ
        nums =[]
        while n not in nums:
            nums.append(n)
            n = kv(n)
        if 1 in nums:
            return True
        else:
            return False


solution = Solution()


print(solution.isHappy(19))
print(solution.isHappy(2))
