"""
Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33,
45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
Посчитать (желательно без использования статистических методов
наподобие std, var, mean) среднее арифметическое, среднее квадратичное
отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.
"""

import math

salary_arr = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57,
              55, 70, 75, 65, 84, 90, 150]
s = salary_arr
print(f'__________________ \n Задаанная выборка = {s} \n__________________')
sum_num = 0
for el in s :
    sum_num += int(el)
average_s = sum_num / len(s)
print(f' - Cреднее арифметическое задаанной выборки = {average_s :.5f}')

st_dev = math.sqrt(sum((el - average_s) ** 2 for el in s) / len(s))
print(f' - Cреднее квадратичное отклонение = {st_dev: .5f}')

variance_bias = sum((el - average_s) ** 2 for el in s) / len(s)
print(' - Смещенная оценка дисперсии = ', variance_bias)

unbiased_variance = sum((el - average_s) ** 2 for el in s) / (len(s) - 1)
print(f' - Несмещенная оценка дисперсии = {unbiased_variance: .5f}')