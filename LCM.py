num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


def calucaltelcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm


print("The L.C.M. of", num1, "and", num2, "is", calucaltelcm(num1, num2))
