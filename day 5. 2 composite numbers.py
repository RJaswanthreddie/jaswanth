choice=input("enter the grade of the employee:")
if(choice=='A'):
    a=int(input("enter employee salary:"))
    if(a>0):
        print("salary=",a)
        b=(0.05 *a)
        print("bonus=",b)
        print("total=",a+b)
elif(choice=='B'):
    c=int(input("enter employee salary:"))
    if(c>0):
        print("salary=",c)
        d=(0.10 *c)
        print("bonus=",d)
        print("total=",c+d)
elif(choice=='C'):
    e=int(input("enter employee salary:"))
    if(e>0):
        print("salary=",e)
        f=(0.02 *e)
        print("bonus=",f)
        print("total=",e+f)
else:
    print("invalid no.!")start = int(input("a="))
end = int(input("b="))
count = 0;
print("Composite Numbers between %d and %d: " % (start, end))
for start in range(start+1, end+1):
    for i in range(1, start+1):
        if(start % i == 0):
            count += 1;
    if(count > 2):
       print(start, end=" ")
    count = 0
