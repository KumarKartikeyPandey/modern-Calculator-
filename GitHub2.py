def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def remainder(a,b):
    return a%b
# Scinetific Calculator without GUI(without tkinter)
import math
while(1):
    print("1. Normal Calculation \n2. Scintific Calculation")
    ch=int(input("Enter your choice for the type of calculation you want to perform:"))
    while ch ==1:
        
        print('''        1. Add
        2. Subtract
        3. Multiplication
        4. Division
        5. Remainder''')
        c1=int(input("Enter the operation you want to perform:"))
        if c1 == 1:
            n1=float(input("Enter First Argument:"))
            n2=float(input("Enter Second Argument:"))
            print("Your Answer is",add(n1,n2))
        elif c1==2:
            n1=float(input("Enter First Argument:"))
            n2=float(input("Enter Second Argument:"))
            print("Your Answer is",sub(n1,n2))
        elif c1 == 3:
            n1=float(input("Enter First Argument:"))
            n2=float(input("Enter Second Argument:"))
            print("Your Answer is",multiply(n1,n2))
        elif c1 == 4:
            n1=float(input("Enter First Argument:"))
            n2=float(input("Enter Second Argument:"))
            print("Your Answer is",divide(n1,n2))
        elif c1 == 5:
            n1=float(input("Enter First Argument:"))
            n2=float(input("Enter Second Argument:"))
            print("Your Answer is",remainder(n1,n2))
        else:
            print("Please enter a valid option!!!!")
            break
    while ch ==2:
        print('''        1.  sinx
        2.  cosx
        3.  tanx
        4.  cotx
        5.  secx
        6.  cosecx
        7.  inverse sinx
        8.  inverse cosx
        9.  inverse tanx
        10. inverse cotx
        11. inverse cosecx
        12. inverse secx
        13. logarithm(base 10)
        14. logarithm(base e)
        15. decimal to binary
        16. decimal to hexadecimal
        17. decimal to octal
        18. Permutation
        19. Combination
        20. a raised to power b
        21. sinhx
        22. coshx
        23. tanhx
        24. Square Root
        25. Factorial of a number
        26. Exponential''')
        ch2=int(input("Enter the operation you want to perform:"))
        if ch2 == 1:
            a1=float(input("Enter the argument:"))
            print("Your answer is",math.sin(a1))
        elif ch2 == 2:
            a1=float(input("Enter the argument:"))
            print("Your Answer is",math.cos(a1))
        elif ch2 == 3:
            a1=float(input("Enter the argument:"))
            print("Your Answer is",math.tan(a1))
        elif ch2 == 4:
            a1=float(input("Enter the argument:"))
            print("Your Answer is",(1/(math.tan(a1))))
        elif ch2 == 5:
            a1=float(input("Enter the argument:"))
            print("Your Answer is",(1/(math.cos(a1))))
        elif ch2 == 6:
            a1=float(input("Enter the argument:"))
            print("Your Answer is",(1/(math.sin(a1))))
        elif ch2 == 7:
            a1=float(input("Enter the argument:"))
            print("Your Answer is",math.asin(a1))
        elif ch2 == 8:
            a1=float(input("Enter the argument:"))
            print("Your Answer is",math.acos(a1))
        elif ch2 == 9:
            a1=float(input("Enter the argument:"))
            print("Your Answer is",math.atan(a1))
        elif ch2 == 10:
            a1=float(input("Enter the argument:"))
            print("Your Answer is",(1/(math.atan(a1))))
        elif ch2 == 11:
            a1=float(input("Enter the argument:"))
            print("Your Answer is",(1/(math.asin(a1))))
        elif ch2 == 12:
            a1=float(input("Enter the argument:"))
            print("Your Answer is",(1/(math.acos(a1))))
        elif ch2 == 13:
            a1=float(input("Enter the argument:"))
            print("Your Answer is",math.log10(a1))
        elif ch2 == 14:
            a1=float(input("Enter the argument:"))
            print("Your Answer is",math.log(a1))
        elif ch2 == 15:
            a1=float(input("Enter the argument:"))
            print("Your Answer is",bin(a1))
        elif ch2 == 16:
            a1=float(input("Enter the argument:"))
            print("Your Answer is",hex(a1))
        elif ch2 == 17:
            a1=float(input("Enter the argument:"))
            print("Your Answer is",oct(a1))
        elif ch2 == 18:
            a1=int(input("Enter the first argument:"))
            a2=int(input("Enter the second argument:"))
            print("Your Answer is",math.perm(a1,a2))
        elif ch2 == 19:
            a1=int(input("Enter the first argument:"))
            a2=int(input("Enter the second argument:"))
            print("Your Answer is",math.comb(a1,a2))
        elif ch2 == 20:
            a1=int(input("Enter the first argument:"))
            a2=int(input("Enter the second argument:"))
            print("Your Answer is",math.pow(a1,a2))
        elif ch2 == 21:
            a1=float(input("Enter the argument:"))
            print("Your Answer is",math.sinh(a1))
        elif ch2 == 22:
            a1=float(input("Enter the argument:"))
            print("Your Answer is",math.cosh(a1))
        elif ch2 == 23:
            a1=float(input("Enter the argument:"))
            print("Your Answer is",math.tanh(a1))
        elif ch2 == 24:
            a1=float(input("Enter the argument:"))
            print("Your Answer is",math.sqrt(a1))
        elif ch2 == 25:
            a1=float(input("Enter the argument:"))
            print("Your Answer is",math.fatorial(a1))
        elif ch2 == 26:
            a1=float(input("Enter the argument:"))
            print("Your Answer is",math.exp(a1))
        else:
            print("Please Enter a valid choice:")
            
