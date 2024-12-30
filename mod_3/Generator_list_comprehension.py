# генераторы - list comprehension - выражения спискового включения!
# генераторы списков позволяют создавать и быстро заполнять списки

# Пример 1. Получим список чисел от 1 до 10 (при помощи функции range): 
numbers = []
for i in range(1, 11):
    numbers.append(i)

# если нужны только четные номера:
numbers = []
for i in range(1, 11):
    if i % 2 == 0:
        numbers.append(i)

# Генераторы списков: выражение возвращающее список в общем виде:
# [ expression for item in list if conditional ]

# Простой пример - есть список - сделаем еще список
a = [1, 2, 3]   # a - итерируемый объект
b = [i+10 for i in a]
print(a, '\n', b)    # [1, 2, 3]  [11, 12, 13] - генератор создает новый список, а не изменяет существующий

# Решение примера 1
# все от 1 до 10:
numbers = [i for i in range(1, 11)]
print(numbers)

# только четные:
numbers = [i**2 for i in range(1, 11) if i % 2 == 0]
print(numbers)


# Пример 2. Есть словарь - получим списки:
a = {1:10, 2:20, 3:30}
b = [[i,a[i]] for i in a]
c = [j for i in b for j in i]
print(a, '\n', b, '\n', c)

# Пример 3: Есть мусор - отберем то, что нужно
st = '15r23edwd93rjf934#$%Ye34F^(*))_+W$#Ddq2)+(ddscew3r'
digits = [i for i in st if i.isdigit()]
letters = [i for i in st if i.isalpha()]
spec_char = [i for i in st if not i.isalnum()]
print('цифры:', *digits)
print('буквы:',*letters)
print('специальные символы:',*spec_char)

# генераторы словарей: возвращают словарь (внешние скобки - фигурные):
#{ key:value for item in list if conditional }

# Пример.
# Дан список словарей, в которых одно из значений используется в качестве идентификатора:
data = [
  {'id': 10, 'data': '...'},
  {'id': 11, 'data': '...'},
  {'id': 12, 'data': '...'},
  {'id': 10, 'data': '...'},
  {'id': 11, 'data': '...'},
]
# требуется удалить повторы 
# Решение на основе генератора словаря:
# создается словарь, ключами которого являются поля, которые приняли за уникальный идентификатор,
# затем с помощью метода values() получаем все значения из созданного словаря
dd = { d['id']:d for d in data }.values()
print(dd)



