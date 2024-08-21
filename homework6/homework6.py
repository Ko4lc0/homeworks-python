names_and_age = {'Sergei': 23, 'Alexsandr': 21, 'Dmitri': 21, 'Anastasia': 19}
print(names_and_age)
print(names_and_age['Sergei'])
print(names_and_age.get('Arseni'))
names_and_age.update({'Kristina': 23, 'Vika': 16})
names_and_age['Alex'] = 24
print(names_and_age)
del names_and_age['Dmitri']
a = names_and_age.pop('Alexsandr')
print(names_and_age)
print(a)
words_and_numbers = {1, 2, 3, 4, 4, 5, 4, 3, 2, 1, 'cat', 'dog', 'dog', 'cat'}
print(words_and_numbers)
print(type(words_and_numbers))
words_and_numbers.update(['parrot', 6])
print(words_and_numbers)
words_and_numbers.remove('cat')  # можно использовать .discard он не выдает ошибку если элемент не найден во множестве
print(words_and_numbers)