lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):
    length = len(str(num))
    sum = 0

    # find the sum of the cube of each digit
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** length
        temp //= 10

    if num == sum:
        print(num)