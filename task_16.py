# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.


length_list = int(input('Введите длину массива: '))
list_int = [int(i) for i in range(1, length_list+1)]
print(f'Дан массив: {list_int}')
number_in_list = int(input('Введите искомое число: '))
print(f'В данном массиве число {number_in_list} встречается {sum([int(list_int[i] == number_in_list) for i in range(len(list_int))])} раз')
