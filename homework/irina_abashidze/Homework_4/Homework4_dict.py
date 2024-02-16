my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [10, 20, 'text2', 40, 50],
    'dict': {'one': 'January', 'two': 'February', 'three': 'March',
             'four': 'April', 'five': 'May'},
    'set': {100, 200, 300, 400, 500}
}

print(my_dict)

# # Для того, что хранится под ключом ‘tuple’ вывести на экран последний элемент
print(my_dict['tuple'][-1])

# добавить в конец списка еще один элемент my_dict['list'] = [10, 20, 'text2', 40, 50, 60]
my_dict['list'].append('60')
# удалить второй элемент списка my_dict['list'] = [10, 'text2', 40, 50, 60]
my_dict['list'].pop(1)

# my_dict['dict'] = {'two': 'February', 'three': 'March',
#                   'four': 'April', 'five': 'May', ('I am a tuple',): 'value6'}
my_dict['dict'][('I am a tuple',)] = 'value6'
my_dict['dict'].pop('one')

# my_dict['set'] = {100, 200, 300, 400, 500, 600}
my_dict['set'].add(600)
# my_dict['set'] = {200, 300, 400, 500, 600}
# my_dict['set'].pop(0)
my_dict['set'].remove(100)
print(my_dict)
