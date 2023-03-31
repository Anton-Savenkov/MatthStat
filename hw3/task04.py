"""
В университет на факультеты A и B поступило равное количество студентов,
а на факультет C студентов поступило столько же, сколько на A и B вместе.
Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8.
Для студента факультета B эта вероятность равна 0.7,
а для студента факультета C - 0.9. Студент сдал первую сессию.
Какова вероятность, что он учится:
a). на факультете A
б). на факультете B
в). на факультете C
"""
#ероятность того, что студент факультета A,B,C сдаст первую сессию
probability_a = 0.8
probability_b = 0.7
probability_c = 0.9

#доля студентов по факультетам
faculty_a = 0.25
faculty_b = 0.25
faculty_c = 0.5

probability_overall = faculty_a * probability_a + faculty_b * probability_b + \
                      faculty_c * probability_c
print(f'Вероятность наступления события P(A) = {probability_overall}')

probability_faculty_a = faculty_a * probability_a / probability_overall
probability_faculty_b = faculty_b * probability_b / probability_overall
probability_faculty_c = faculty_c * probability_c / probability_overall

print(f' - Вероятность того, что студент учится на факультете А = '
      f'{probability_faculty_a:.4f} ---> {probability_faculty_a * 100:.2f}%\n'
      f' - Вероятность того, что студент учится на факультете B = '
      f'{probability_faculty_b:.4f} ---> {probability_faculty_b * 100:.2f}%\n'
      f' - Вероятность того, что студент учится на факультете C = '
      f'{probability_faculty_c:.4f} ---> {probability_faculty_c * 100:.2f}%')