#Simple Calculator Program
print("-Simple Calculator-")
print('Please choose an operation')
print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')

input_num=input()

if input_num == '1':
    print('Addition')
    firstnum=input('Enter your first number:')
    secondnum=input('Enter your second number:')
    print('Total: ' + str(int(firstnum) + int(secondnum)))

elif input_num == '2':
    print('Subtraction')
    firstnum=input('Enter your first number:')
    secondnum=input('Enter your second number:')
    print('Total: ' + str(int(firstnum) - int(secondnum)))

elif input_num == '3':
    print('Multiplication')
    firstnum=input('Enter your first number:')
    secondnum=input('Enter your second number:')
    print('Total: ' + str(int(firstnum) * int(secondnum)))

elif input_num == '4':
    print('Division')
    firstnum=input('Enter your first number:')
    secondnum=input('Enter your second number:')
    print('Total: ' + str(int(firstnum) / int(secondnum)))

else:
    print('Please try again')







