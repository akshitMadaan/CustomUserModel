x = int(input("Enter the value of x:"))
print (x)
print(type(x))
n = int(input("Enter the value of n:"))
print(n)
print(type(n))
sum=0
def first(x,n):
    sum=0
    for i in range(1,n+1):
        sum += 1/x**i
    print(sum)
first(x,n)

def second(x,n,sum):
    if n==0:
        return 0
    else:
        sum = 1/(x**n) + second(x,(n-1),sum)
        return sum

x = second(x,n,sum)
print(x)

