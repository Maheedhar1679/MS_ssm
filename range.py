x = range(1,50)
for num in x:
    if num % 3 == 0 :
        print("fizz")
    else:
        if num % 5 == 0:
            print("buzz")
        else:
            print(num)
