
#fibanochhi program

num = int(input("gimme a number "))

if num == 0:
    print("Fib is " + str(num))
elif num == 1:
    print("fib is 0 1")
else:
    x = 1
    last = 1
    lastlast = 0
    print("Fib is " + str(lastlast) + " ", end='')
    while x < num:
        print(str(last) + " ", end='')
        temp = last
        last = lastlast + last
        lastlast = temp
        x+=1

