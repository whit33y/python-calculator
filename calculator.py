result = 0
chosen_operation_check = False
while chosen_operation_check == False:
    chosen_operation = input('a=add, s=subtract, m=multiply, d=divide, e=exit, r=reset: ')
    if chosen_operation == 'e':
        chosen_operation_check = True
    elif chosen_operation == 'a' or chosen_operation == 's' or chosen_operation =='m' or chosen_operation =='d':
        if result == 0:
            result = float(input('Give number: '))
            print(result,'')
            chosen_number = float(input('Give number: '))
            if chosen_operation == 'a':
                result = result + chosen_number
                print(result)
            elif chosen_operation == 's':
                result = result - chosen_number
                print(result)
            elif chosen_operation == 'm':
                result = result*chosen_number
                print(result)
            elif chosen_operation == 'd':
                result = result/chosen_number
                print(result) 
        else:
            chosen_number = float(input('Give number: '))
            if chosen_operation == 'a':
                result = result + chosen_number
                print(result) 
            elif chosen_operation == 's':
                result = result - chosen_number
                print(result)
            elif chosen_operation == 'm':
                result = result*chosen_number
                print(result)
            elif chosen_operation == 'd':
                result = result/chosen_number
                print(result) 
    elif chosen_operation == 'r':
        result = 0
    else:
        print('I dont get it')
        chosen_operation==False


