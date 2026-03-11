a = 12
b = 3
print(a + b)#15
print(a - b)#9
print(a * b)#36
print(a / b)#4.0
print(a//b) #integer division
print(a % b)#modulo operator

print()
for i in range(1,a//b):#float can't be interpreted as integer 
    print(i)
    
#practice
buns_price = 2.40
customer_money = 15
print(customer_money//buns_price)

#operators precedence
print(a + b/ 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print((((a + b) /3) -4) * 12)
print(((a + b) / 3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)