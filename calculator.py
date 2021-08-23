import math
import re
while 1 == 1:
    valid_color = ['red',
        'green',
        'gray',
        'blue',
        'purple',
        'yellow'
    ]
    valid_time = {
        'minute':'minute',
        'minutes':'minutes',
        'second':'second',
        'seconds':'seconds',
        'hour':'hour',
        'hours':'hours'
    }
    t = 0
    w = 0
    
    
    
    while True:
        z = input('Which color of science are you trying to make? ').lower()
        if z in valid_color[0]:

            w += 11
            x = 5
            break

        elif z in valid_color[1]:

            w += 16
            x = 6
            break

        elif z in valid_color[2]:

            w += 13
            x = 10
            break

        elif z in valid_color[3]:

            w += 24
            x = 24
            break

        elif z in valid_color[4]:

            w += 19
            x = 21
            break

        elif z in valid_color[5]:

            w += 44
            x = 21
            break
        
        elif z == 'white':
            print('Sorry, that item is uncraftable!')

        else:

            print('Please input a valid color. Valid colors are \n')
            print(valid_color)
            print('\nRemember, white science cannot be crafted.')

    while True:
        try:
            n = int(input('How many would you like to make? '))
            break
        except ValueError:
            print('Please only enter integers!')
        
    while True:
        try:
            answer = input('How long are you willing to wait? ').lower()
            words = answer.split()
            words[1] in valid_time
            break
                
        except IndexError:
            print('Please enter a valid time')
        
    y = int(re.search(r'\d+', answer).group())



    if valid_time['seconds'] or valid_time['second'] in answer:

        t += 1
        arrays = int(math.ceil(x * (4/3) * n / t / w / y))
        factories = int(math.ceil(x * (4/3) * n / t / y))

        print('You need ' + str(factories) + ' factories, or just under ' + str(arrays) + ' arrays')

    elif valid_time['minute'] or valid_time['minutes'] in answer:

        t += 60
        arrays = int(math.ceil(x * (4/3) * n / t / w / y))
        factories = int(math.ceil(x * (4/3) * n / t / y))

        print('You need ' + str(factories) + ' factories, or just under ' + str(arrays) + ' arrays')

    elif valid_time['hour'] or valid_time['hours'] in answer:

        t += 3600
        arrays = int(math.ceil(x * (4/3) * n / t / w / y))
        factories = int(math.ceil(x * (4/3) * n / t / y))

        print('You need ' + str(factories) + ' factories, or just under ' + str(arrays) + ' arrays')
