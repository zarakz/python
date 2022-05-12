# a program to calculate the square root

def square_root(number):
    error = 0.01
    guess = number / 2
    iteration = 0
    while (abs(number - pow(guess, 2))) > error:
        iteration += 1
        taghsim = number / guess
        guess = (taghsim + guess)/2
    print("The square root of", number, " is ", guess)


flag = True

while flag:
    square_root_want = input("do you want compute any square root?(y/n): ")
    if square_root_want == "y":
        x = input("give me your number, I give you back the square root of it: ")
        square_root(float(x))
    else:
        flag = False
        break


