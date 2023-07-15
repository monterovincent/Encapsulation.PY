class Occupation:
    def __init__(engineer, name, age, gender,mail,sal,engr_type):
        engineer.name = name
        engineer.age = age
        engineer.gender = gender
        engineer.mail = mail
        engineer.sal = sal
        engineer.engr_type = engr_type

    def occupation_info(engineer):
             return f'{engineer.name} {engineer.age} {engineer.gender} {engineer.mail} {engineer.sal} {engineer.engr_type}'


occupation1 = Occupation('dave',23, 'male','kasava@mail.com',  345567  ,   'civil engineer' )
print(occupation1.occupation_info())