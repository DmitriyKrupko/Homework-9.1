from Func import gen_list, modify_list
x = int(input('Введите первое число для списка: '))
y = int(input('Введите второе число для списка: '))
print(gen_list(x, y))
print(modify_list(lst=gen_list(x, y)))
