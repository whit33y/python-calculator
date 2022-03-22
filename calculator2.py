def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
result = 0
while True:
    choice = input('a-add s-subtract m-multiply d-divide ')
    if choice in('a','s','m','d'):
        if result == 0:
            num1 = float(input('Enter number: '))
            num2 = float(input('Enter number: '))
            if choice == 'a':
                result = add(num1, num2)
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == 's':
                result = subtract(num1, num2)
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == 'm':
                result = multiply(num1, num2)
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == 'd':
                result = divide(num1, num2)
                print(num1, "/", num2, "=", divide(num1, num2))
        else:
            num2 = float(input('Enter number: '))
            if choice == 'a':
                print(result, "+", num2, "=", add(result, num2))
                result+=num2
            elif choice == 's':
                print(result, "-", num2, "=", subtract(result, num2))
                result-=num2
            elif choice == 'm':
                print(result, "*", num2, "=", multiply(result, num2))
                result*=num2
            elif choice == 'd':
                print(result, "/", num2, "=", divide(result, num2))
                result/=num2 
    else:
        print('I dont know it')