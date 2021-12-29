

num = int(input('What number do you want to use? '))

# message = 'positive' if num > 0 else '0 or negative'
# use ^ when only 2 conditions

if num > 0:
    print(f'{num} is positive')
elif num == 0:
    print(f'{num} is zero')
else:
    print(f'{num} is negative')
