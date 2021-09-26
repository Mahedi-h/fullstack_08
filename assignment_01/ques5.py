list = [10,50,90,55,155,163,222,325]
for i in list:
    if (i % 5 == 0):
        if i > 150:
            print('the number is greater than 150')
            break
        else:
            print('the number is=',i)