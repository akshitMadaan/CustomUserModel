def eqn(x,y,a,b):
    val=0
    val= (x/y)**(a+b)
    print(val)

x, y, a, b = map(int,input("Enter x,y,a,b values: ").split())

eqn(x,y,a,b)
