def foo(a,b,n=100):
    x=a
    dx=(b-a)/n
    while x<=b:
        print("x=",x," sqrt(x)=",x**0.5)
        x+=dx