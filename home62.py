# 2 – Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности,
# список повторяемых и убрать дубликаты из заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

from itertools import count


lst = [1, 2, 3, 5, 1, 5, 3, 10]
nonRepeatElem = []
repeatElem = []
for i in lst:
    if lst.count(i) == 1:
        nonRepeatElem.append(i)
    else:
        repeatElem.append(i)

print(f'Исходный список:\n{lst}')
print(f'Список без дубликатов:\n{list(set(lst))}')
print(f'Список неповторяемых элементов:\n{nonRepeatElem}')
print(f'Список повторяемых элементов:\n{list(set(repeatElem))}')
