num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime No")
            print("{} times of {} is {}".format(i, int(num/i), num))
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime No")