def pow(y,z):
    return(y**z)
def add(y,z):
    return(y+z)
def sub(y,z):
    return(y-z)
def mul(y,z):
    return(y*z)
def div(y,z):
    return(y/z)
a=int(input("select any operation:\n"
      "1.power\n"
      "2.addition\n"
      "3.subtraction\n"
      "4.multiplication\n"
      "5.division\n"))
x=int(input("enter the first number: "))
n=int(input("enter the second number: "))
if(a==1):
    print(x,"**",n,"=",pow(x,n))
elif(a==2):
    print(x,"+",n,"=",add(x,n))
elif(a==3):
    print(x,"-",n,"=",sub(x,n))
elif(a==4):
    print(x,"*",n,"=",mul(x,n))
elif(a==5):
    print(x,"/",n,"=",div(x,n))
else:
    print("invalid input")
