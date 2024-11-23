immutable_var = 1, True, 'python', [1, 2, 3, 4]
print(immutable_var)
#   immutable_var[1] = False - невозможно изменить значение кортежа
immutable_var[3][2] = 122   # кортеж сам по себе является неизменяемым, но списки в нем изменять можно
print(immutable_var)
mutable_list = [1, 10, 2, 133]
mutable_list[1] = 'fine'
print(mutable_list)