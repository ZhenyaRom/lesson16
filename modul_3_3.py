def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(1, 2, 3)
print_params(c = False, a = 'четыре')
print_params(b = 'str')
print_params(c = [1,2,3])


values_list = ['Hi', False, 14]
print_params(*values_list)
values_dict = {'a': 8, 'b': 'good', 'c': -2}
print_params(**values_dict)


values_list2 = ['S', 56.3]
print_params(*values_list2, 42)
