
number = 23

guess = int(input('{} Enter an integer: '.format(number) ))

if (guess == number):
    print('guess == number')
elif (guess < number):
    print('guess < number')
else:
    print('guess > number')

print('done')