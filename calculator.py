def operation(operation,user_number,result):
    if operation == 'a':
        result+=user_number
        return result
    elif operation == 's':
        result-=user_number
        return result  
    elif operation == 'm':
        result = result * user_number
        return result
    else:
        return('Wrong') 
result = 0
chosen_operation_check = False
while chosen_operation_check == False:
    chosen_operation = input('a=add, s=subtract, m=multiply, e=exit: ')
    if chosen_operation == 'e':
        chosen_operation_check = True
    else:
        if result == 0:
            result = int(input('Give number: '))
            chosen_number = int(input('Give number: '))
            print(operation(chosen_operation,chosen_number,result))
            result+=chosen_number
        else:
            chosen_number = int(input('Give number: '))
            print(operation(chosen_operation,chosen_number,result))
            if chosen_operation == 'a':
                result+=chosen_number 
            elif chosen_operation == 's':
                result-=chosen_number 
            elif chosen_operation == 'm':
                result = result*chosen_number 


