#Lab 5 Python
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    if n>1:
        return fib(n-1)+fib(n-2)

el1 = 1
el2 = 2 
sum = 0
while el1 <= 4000000:
    if el1 % 2 == 0:
        sum += el1
        print(el1)
    el1, el2 = el2, el1 + el2     
print (sum)

#Lab 5 Python

