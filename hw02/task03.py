"""
Монету подбросили 144 раза.
Какова вероятность, что орел выпадет ровно 70 раз?
"""

from myfunkmathstat import funk_Bernoulli

n = 144
k = 70
p = 0.5


print(f'Вероятность того, что орел выпадет ровно 70 раз = '
      f'{funk_Bernoulli(n,k,p):.5f} -> {funk_Bernoulli(n,k,p)*100:1.2f}%')