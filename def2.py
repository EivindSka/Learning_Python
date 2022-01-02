
def is_adult(age):
    if age >= 16:
        return True
    else:
        return False


def convertGender(gender='unknown'):
    if gender.upper() == 'M':
        return 'Male'
    elif gender.upper() == 'F':
        return 'Female'
    else:
        return f'Gender {gender} is unknown'


result = is_adult(80)
print(result)


print(convertGender('F'))
print(convertGender('M'))
print(convertGender('f'))
print(convertGender('m'))
print(convertGender('hello'))
