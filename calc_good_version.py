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
    choice = input('a-add s-subtract m-multiply d-divide r-reset e-exit ')
    if choice == 'e':
        exit()
    if choice in('a','s','m','d','r'):
        if result == 0:
            while True:
                try:
                    if choice == 'a':
                        num1 = float(input('Enter number: '))
                        num2 = float(input('Enter number: '))
                        result = add(num1, num2)
                        print(num1, "+", num2, "=", add(num1, num2))
                        break
                    elif choice == 's':
                        num1 = float(input('Enter number: '))
                        num2 = float(input('Enter number: '))
                        result = subtract(num1, num2)
                        print(num1, "-", num2, "=", subtract(num1, num2))
                        break
                    elif choice == 'm':
                        num1 = float(input('Enter number: '))
                        num2 = float(input('Enter number: '))
                        result = multiply(num1, num2)
                        print(num1, "*", num2, "=", multiply(num1, num2))
                        break
                    elif choice == 'd':
                        num1 = float(input('Enter number: '))
                        num2 = float(input('Enter number: '))
                        result = divide(num1, num2)
                        print(num1, "/", num2, "=", divide(num1, num2))
                        break
                    elif choice == 'r':
                        result = 0
                        print(result)
                        break
                except ValueError:
                    print('We need int or float')
            
        else:
            while True:
                try:
                    if choice == 'a':
                        num2 = float(input('Enter number: '))
                        print(result, "+", num2, "=", add(result, num2))
                        result+=num2
                        break
                    elif choice == 's':
                        num2 = float(input('Enter number: '))
                        print(result, "-", num2, "=", subtract(result, num2))
                        result-=num2
                        break
                    elif choice == 'm':
                        num2 = float(input('Enter number: '))
                        print(result, "*", num2, "=", multiply(result, num2))
                        result*=num2
                        break
                    elif choice == 'd':
                        num2 = float(input('Enter number: '))
                        print(result, "/", num2, "=", divide(result, num2))
                        result/=num2 
                        break
                    elif choice == 'r':
                        result=0
                        print(result)
                        break
                except ValueError:
                    print('We need int or float')
    else:
        print('I dont know it')