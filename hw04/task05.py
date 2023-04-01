"""
На сколько сигм (средних квадратичных отклонений) отклоняется рост человека,
равный 190 см, от математического ожидания роста в популяции,
в которой M(X) = 178 см и D(X) = 25 кв.см?
"""
from math import sqrt

item_height = 190
average_height = 178
dispersion = 25
std = sqrt(dispersion)
sigma = (item_height - average_height) / std
print(f'\nРост человека = {item_height}см, отклоняется от математического ожидания '
      f'роста в популяции, со средним роостом {average_height} '
      f'на {sigma} сигм.')