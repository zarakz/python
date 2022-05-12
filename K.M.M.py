def LCM(num1, num2):
    list1 = []
    if num1 < num2:
        temp = num1
    else:
        temp = num2
    for i in range(2, temp+1):
        if num1 % i == 0 and num2 % i == 0:
            num1 = num1 / i
            num2 = num2 / i
            list1.append(i)
    list1.append(int(num1))
    list1.append(int(num2))
    print(list1)

    def list_multiple(list_sub):
        multiple = 1
        for item in list_sub:
            multiple *= item
        return multiple

    lcm = list_multiple(list1)
    return lcm


number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
print(LCM(number1, number2))
