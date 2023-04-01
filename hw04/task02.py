"""
О случайной непрерывной равномерно распределенной величине B известно,
что ее дисперсия равна 0.2. Можно ли найти правую границу величины B
и ее среднее значение зная, что левая граница равна 0.5?
Если да, найдите ее.
"""

a = 0.5
d = 0.2
right_border = a + (d * 12) ** (1 / 2)

print(f'Правая граница величины В = {right_border: .3f}'
      f'\nСреднее значение В на промежутке от {a} до {right_border: .3f}'
      f' ровна {(right_border + a) / 2: .3f}')