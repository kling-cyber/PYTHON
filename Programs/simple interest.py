#wap to calculate simple interest
p = float(input("Enter the principal amount: "))
r= 5
n= float(input("Enter the time in years: "))
si = (p * r * n) /100  
print("The simple interest is:", si)    

#wap to calculate compound interest using power function using formula ci = p*(1+r/n)^nt)   
import math
pc = float(input("Enter the principal amount: "))
rc = 5       
t = float(input("Enter the time in years: "))      
ci = pc *(math.pow((1 + rc / 100),t)) - pc
print("The compound interest is:", ci)  
