def addition(list):
    result = 0
    for a in list:
        result+=a
    return result
def subtraction(list):
    result = list[0]
    for a in range (1,len(list)):
        result-=list[a]
    return result
while True:
    try:
        how_much_numbers = int(input("How much numbers: "))
        what_operation = int(input("Type 1 to add numbers, type 2 to subtract: "))
        break
    except ValueError:
        print("Int, please.")
if(what_operation==1):
    for a in range(how_much_numbers):
        print('Addition')
if(what_operation==2):
    for a in range(how_much_numbers):
        print('Subtraction')
