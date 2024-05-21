a1=float(input("Enter the First equation's 'x' coefficient : "))
b1=float(input("Enter the First equation's 'y' coefficient : "))
c1=float(input("Enter the First equation's 'z' coefficient : "))
o1=float(input("Enter the First equation's RHS: "))
a2=float(input("Enter the Second equation's 'x' coefficient : "))
b2=float(input("Enter the Second equation's 'y' coefficient : "))
c2=float(input("Enter the Second equation's 'z' coefficient : "))
o2=float(input("Enter the Second equation's RHS: "))
a3=float(input("Enter the Third equation's 'x' coefficient : "))
b3=float(input("Enter the Third equation's 'y' coefficient : "))
c3=float(input("Enter the Third equation's 'z' coefficient : "))
o3=float(input("Enter the Third equation's RHS: "))
y1=0
z1=0
z2=0
for p in range(25):
    x=(1/a1)*((o1)-(b1*y1)-(c1*z1))
    x2=x
    y=(1/b2)*((o2)-(a2*x2)-(c2*z2))
    x3=x2
    y3=y
    z=(1/c3)*((o3)-(a3*x3)-(b3*y3))
    y1=y
    z1=z
    z2=z
print("x=",x,"  y=",y," z=",z)
