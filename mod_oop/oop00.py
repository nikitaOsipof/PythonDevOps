
class Person:
    status = "Специалист"   # атрибут класса

    """        
    метод класса работает с атрибутом класса
    """

    def display_str():
        return "Приветвенное имя: Уважаемый {}".format(Person.status)


def display_info(pers):
    print("Имя: ", pers.name)
# Использование метода класса

display_info(Person)
stPerson = Person.display_str()

print(Person)
print(stPerson)

p = Person()
p.display_str() # TypeError: display_str() takes 0 positional arguments but 1 was given

d = Person()
#p.display_info()    # TypeError: display_info() takes 0 positional arguments but 1 was given
print(p.name, d.name)

p.name = "Polo" # атрибут объекта - создан новый
print(p.name)

f = Person()
print(Person.name, f.name)
