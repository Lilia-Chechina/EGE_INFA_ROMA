# # "Дана переменная a = 7 и переменная b = 5, вывести на экран результат их:
# # сложения, вычитания,
# # целочисленного деления, обычного деления, умножения (*), остаток(%)."
#
# a = 7
# b = 5
# print(a+b, a-b, b-a, a//b, a/b, a*b, a%b)

# "Пройтись циклом от 1 до 7 с помощью 1) for 2) while и вывести чётные числа, то есть те,
#  остаток деления которых на 2 = 0."

# for i in range(1, 8): # от 1 до 7
#     # 3 параметром цикла for можно задать шаг
#     if i % 2 == 0:
#         print(i)

# j = 1
# while (j != 8):
#     if j % 2 == 0:
#         print(j)
#     j+=1

# "Инициализировать пустой список с названием sps. Добавить в список с помощью append числа: 3, 27, 888.
# Затем удалить элемент списка 1) по значению: 3; 2) по индексу второй элемент, т.е индекс = 1."
sps = []
sps.append(3)
sps.append(27)
sps.append(888)
print(sps)
print(*sps)
sps.remove(3) # удаление по значению
print(sps)
print(len(sps))
print(sps.pop(1)) # возвращаем эл-т, который удалили
print(sps)
