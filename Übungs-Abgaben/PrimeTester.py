## @Felix_Regler 
## Version: 1.0
## 10.11.2023

## Exercise_1: primenumber checker
## The task of the program is to check whether a number, entered by the user, is prime.
## (A prime number is only completely divisible by itself and 1)

## initialization of relevant variables
prime = True;
x = float(input("Please insert the number you would like to check:  "));
qou = x;
div = 2;

## Check for 0; negetive Numbers and decimal places
if x == 0:
    print("Youre not allowed to devide by 0!");
    exit();
if x < 0:
    print("A negative Number cant be a primenumber!")
    exit();
if x % 1 == 0:
    ##If the quotient becomes smaller than the quotient, you have already checked every possible integer division and can therefore end the iteration
    while div < qou:
        qou = x / div;
        ##if the quotient has no decimal places, a number is completely divisible by the divsor
        if qou % 1 == 0:
            prime = False
            break;
        else:
            div += 1;  
else:
    prime = False;
    print("Your number has some decimal places, therefor it cant be a primenumber!");

if prime:
    print("Your number is a primenumber!");
else:
    print("Your number is not a primenumber, it`s completely divisible by: " , div , " and " , qou);