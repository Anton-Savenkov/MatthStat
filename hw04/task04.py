"""
Рост взрослого населения города X имеет нормальное распределение.
Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
а). больше 182 см
б). больше 190 см
в). от 166 см до 190 см
г). от 166 см до 182 см
д). от 158 см до 190 см
е). не выше 150 см или не ниже 190 см
ё). не выше 150 см или не ниже 198 см
ж). ниже 166 см.
"""
from scipy.stats import norm

average_height = 174
st_dev = 8

a, b = 182, 190

probability_a = 1 - norm.cdf(a, average_height, st_dev)
print(f'Вероятность роста больше {a}см ={probability_a: .4f}')

probability_b = 1 - norm.cdf(b, average_height, st_dev)
print(f'Вероятность роста больше {b}см ={probability_b: .4f}')

v_min, v_max = 166, 190
probability_v = norm.cdf(v_max, average_height, st_dev) - \
                norm.cdf(v_min, average_height, st_dev)
print(f'Вероятность роста от {v_min}см до {v_max}см ={probability_v: .4f}')

g_min, g_max = 166, 182
probability_g = norm.cdf(g_max, average_height, st_dev) - \
                norm.cdf(g_min, average_height, st_dev)
print(f'Вероятность роста от {g_min}см до {g_max}см ={probability_g: .4f}')

d_min, d_max = 158, 190
probability_d = norm.cdf(d_max, average_height, st_dev) - \
                norm.cdf(d_min, average_height, st_dev)
print(f'Вероятность роста от {d_min}см до {d_max}см ={probability_d: .4f}')

e_min, e_max = 150, 190
probability_e = norm.cdf(e_min, average_height, st_dev) + 1 - \
                norm.cdf(e_max, average_height, st_dev)
print(f'Вероятность роста не выше {e_min}см или '
      f'не ниже {e_max}см ={probability_e: .4f}')

i_min, i_max = 150, 198
probability_i = norm.cdf(i_min, average_height, st_dev) + 1 - \
                norm.cdf(i_max, average_height, st_dev)
print(f'Вероятность роста не выше {i_min}см или '
      f'не ниже {i_max}см ={probability_i: .4f}')

j = 166
probability_j = norm.cdf(j, average_height, st_dev)
print(f'Вероятность роста ниже {j}см ={probability_j: .4f}')