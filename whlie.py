#i = 0
#while i <  10 :
 #   print("*" * i)
 #   i = i + 1



i = 1
while i <= 100 :
    n1 = i%10
    n2 = i//10
    if n1%3 == 0 and  n2%3!= 0  :
        print('**')
    if n1%3 == 0 or  n2%3!= 0  :
        print('*')

    print(i)


    i += 1
