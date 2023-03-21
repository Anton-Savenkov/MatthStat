"""
В первом ящике находится 10 мячей, из которых 7 - белые.
Во втором ящике - 11 мячей, из которых 9 белых.
Из каждого ящика вытаскивают случайным образом по два мяча.
 - Какова вероятность того, что все мячи белые?
 - Какова вероятность того, что ровно два мяча белые?
 - Какова вероятность того, что хотя бы один мяч белый?
"""
from myfunkmathstat import funk_Probability
f = funk_Probability #для сокращения записи расчетаа

#Какова вероятность того, что все мячи белые из двух случайных
probability_that_all_balls_are_white = \
    f(7, 2) * f(3, 0) / f(10, 2) * f(9, 2) * f(2, 0) / f(11, 2)
print(f'Вероятность, что все мячи белые = '
      f'{probability_that_all_balls_are_white:.5f} ---> '
      f'{probability_that_all_balls_are_white *100:0.2f}%')

#Какова вероятность того, что ровно два мяча белые
probability_that_exactly_two_balls_are_white = \
    f(7, 2) * f(3, 0) / f(10, 2) * f(9, 0) * f(2, 2) / f(11, 2) + f(7, 1)\
    * f(3, 1) / f(10, 2) * f(9, 1) * f(2, 1) / f(11, 2) + f(7, 0) \
    * f(3, 2) / f(10, 2) * f(9, 2) * f(2, 0) / f(11, 2)

print(f'Вероятность, что ровно два мяча белые = '
      f'{probability_that_exactly_two_balls_are_white:.5f} ---> '
      f'{probability_that_exactly_two_balls_are_white * 100:0.2f}%')

#Какова вероятность того, что хотя бы один мяч белый
probability_that_at_least_one_ball_is_white = \
    1 - f(7, 0) * f(3, 2) / f(10, 2) * f(9, 0) * f(2, 2) / f(11, 2)

print(f'Вероятность, что хотя бы один мяч белый = '
      f'{probability_that_at_least_one_ball_is_white:.5f} ---> '
      f'{probability_that_at_least_one_ball_is_white * 100:0.2f}%')