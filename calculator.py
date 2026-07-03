                               
                             #__Simple Python Calculator__#


a=int(input('give a integer:'))          #Here first number is taken as input from user


operation=input('give a operation like:+,-,*,/,//,%,**,&,|,^:')   #asking for operation 


b=int(input('give another integer'))          #second number is taken as input from user

if operation=='+':                            #Addition
    
    print(a+b)

elif operation=='-':                          #Subtraction
    
    print(a-b)

elif operation=='*':                          #Multiplication
    
    print(a*b)

elif operation=='/':                          #Division
    if b==0:
     print('denominator can\'t be zero')
    else:
     print(a/b)

elif operation=='**':                         #Exponent
    
    print(a**b)
    
elif operation=='//':                         #Floor division
    if b==0:
        print('denominator can\'t be zero')
    
        print(a//b)    

elif operation=='%':                          #Remainder
   if b==0:
       print('denominator can\'t be zero')
   else:
     print(a%b)

elif operation=='&':                          #AND Gate
    
    print(a&b)
    
elif operation=='|':                          #OR Gate
    
    print(a|b)
    
elif operation=='^':                          #XOR Gate
    
    print(a^b)
    
else:
    
    print('Invalid operation')