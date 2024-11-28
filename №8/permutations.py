# Петя составляет шестибуквенные слова.
# Слова составляются из букв слова "АВРОРА".
# Петя не использует слова с двумя одинаковыми буквами подряд.
# Сколько различных слов может составить Петя?


# в product буквы могут повторяться
# в permutations(перестановках) не могут

from itertools import permutations
count = 0
for i in permutations('АВРОРА'):
    flag=True
    for j in range(0, 4 + 1):
        if i[j] == i[j + 1]:
            flag=False # им мы прерываем цикл for с j
            break
    if flag==True:
        count+=1
print(count)
# В множестве set элементы не потворяются



