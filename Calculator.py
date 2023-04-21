#Defining the Operation
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

print('Select the Operation')
print('1. Addition')
print('2. Subraction')
print('3. Multiplication')
print('4. Division')

#Entering the user defined input
choice = input('Select the Operation(1/2/3/4)')
num1 = float(input('Enter the First number :-'))
num2 = float(input('Enter the second number :-' ))

if choice == '1':
    print(num1,'+',num2,'=',add(num1,num2))
    
elif choice == '2':
    print(num1,'-',num2,'=',sub(num1,num2))
    
elif choice == '3':
    print(num1,'*',num2,'=',mul(num1,num2))
    
elif choice == '4':
    print(num1,'/',num2,'=',div(num1,num2))
    
else:
    print("Invalid Operation")