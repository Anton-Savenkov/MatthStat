"""
Устройство состоит из трех деталей. Для первой детали вероятность выйти
из строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25.
Какова вероятность того, что в первый месяц выйдут из строя:
а). все детали
б). только две детали
в). хотя бы одна деталь
г). от одной до двух деталей?
"""

#вероятность выйти из строя для 1-й, 2-й, 3-й детали
item_one = 0.1
item_two = 0.2
item_three = 0.25

#вероятность выйти из строя в первый месяц для всех деталей
probability_overall = item_one * item_two * item_three
print(f' - Вероятность того, что из строя выйдут все детали = '
      f'{probability_overall:.3f} ---> {probability_overall * 100:.2f}%')

probability_for_two_item = item_one * item_two * (1 - item_three) + item_one *\
                           item_three * (1 - item_two) + item_two * \
                           item_three * (1 - item_one)
print(f' - Вероятность того, что из строя выйдут только 2 детали = '
      f'{probability_for_two_item:.2f} ---> '
      f'{probability_for_two_item * 100:.2f}%')

probability_for_one_item = 1 - (1 - item_one) * (1 - item_two) * \
                           (1 - item_three)
print(f' - Вероятность того, что из строя выйдет хотя бы одна деталь = '
      f'{probability_for_one_item:.2f} ---> '
      f'{probability_for_one_item * 100:.2f}%')

print(f' - Вероятность того, что выйдут из строя от одной до двух деталей = '
      f'{probability_for_one_item + probability_for_two_item:.3f} ---> '
      f'{(probability_for_one_item + probability_for_two_item) * 100:.2f}%')