my_dict = {'Ilya': 1997, 'Dima': 1996, 'Andrey': 1995}
print(my_dict)
print(my_dict.get('Ilya'))
print(my_dict.get('Artem'))
my_dict.update({'Artem': 1997,
                'Konstantin': 2003})
print(my_dict)
konstantin = my_dict.pop('Konstantin')
print(konstantin)
print(my_dict)
my_set = {1, 1, 1, 2, 4, 3, 4, 6, 5, 3, 2, 8, 'python', 'python', 8}
print(my_set)
my_set.add(10)
my_set.add(11)
print(my_set)
my_set.discard('python')
print(my_set)