class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age= age
        self.__gender = gender
        self.salary = 0.0

    def __str__(self):
       return f'my name is {self.__name} age is {self.__age} {self.__gender}'
    def get_name(self):

        return self.__name

    def set_name(self, name):
        self.__name = name
    def del_name(self):

            del self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
         self.__age = age

    def del_age(self):
        del self.__age

    def get_gender(self):
            return self.__gender

    def set_gender(self, gender):

         self.__gender = gender

    def del_gender(self):
            del self.__gender

    name = property(get_name,set_name,del_name)
    age= property(get_age, set_age, del_age)
    gender = property(get_gender, set_gender, del_age)


p1= Person('dave',23, 'male')
p1.name = 'ruth'
p1.gender = 'female'
print(p1.gender)
# print(p1.set_age(34))
# print(p1.set_gender('male'))
# print(p1.set_name('carlos'))
# print(p1.get_name())
# print(p1.get_age())
# print(p1.get_gender())