"""
formatted strings
"""

name = 'Guido'
age = 56

print(f'{name} is {age} years old.')

userInfo = '{} is {} years old.'

print(userInfo.format(name, age))

userInfo2 = '{name} is {age} years old.'

print(userInfo2.format(name=name, age=age))

userinfo3 = '{0} is {1} years old.'.format(name, age)

print(userinfo3)

userInfo4 = '{} is {} years old.'.format('Guido', 56)

print(userInfo4)

userInfo5 = '{name} is {age} years old.'.format(name='Guido', age=56)

userInfo6 = f'{name} is {age} years old.'

print(userInfo6)
