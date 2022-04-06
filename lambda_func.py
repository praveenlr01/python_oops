add=lambda a,b:print(a+b)
sub=lambda a,b:print(a-b)
mul=lambda a,b:print(a*b)
div=lambda a,b:print(a/b)

while True:
    opt=int(input("[1]addition [2]subtraction [3]multiplication [4]Division\nEnter:"))
    a=int(input("Enter a value: "))
    b=int(input("Enter b value: "))
    if opt==1:
        add(a,b)
    elif opt==2:
        sub(a,b)
    elif opt==3:
        mul(a,b)
    elif opt==4:
        div(a,b)
    else:
        print("Invalid Entery.")
