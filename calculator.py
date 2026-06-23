def add(P, Q):
    return P + Q
def subtract(P, Q):
    return P - Q
def multiply(P, Q):
    return P * Q
def divide(P, Q):
    return P / Q
print('Please select an operation')
print('A. addition')
print('B. Subtraction')
print('C. multiplication')
print('D. division')
choice = (input('Please enter your choice(A/B/C/D):'))
num1 = int(input('type the first number:'))
num2 = int(input('type the second number:'))
if choice == 'A':
    print(num1, '+', num2, '=' , add(num1, num2))
elif choice == 'B':
    print(num1, '-', num2 ,'=' ,subtract(num1, num2))
elif choice == 'C':
    print(num1, '*', num2, '=', multiply(num1,num2 ))
elif choice == 'D':
    print(num1, '/', num2, '=', divide(num1,num2))
else:
    print('Invalid')

