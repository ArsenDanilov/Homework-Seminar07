def print_operation_table(op, rows, columns):
    for i in range (1, rows + 1):
        for j in range (1, columns + 1):
            print(i*j, end = "\t")
        print()

rows = int(input('Введите колво рядов'))
columns = int(input('Введите колво столбцов'))
print(print_operation_table(lambda x,y: x*y, rows, columns))


# my_list = [1, 2, 3, 4, 5, 6, 7]
# my_list2 = list(filter(lambda x: x % 2 == 0, my_list)) # очень быстрая сортировка по любым параметрам 
# print(my_list2)
