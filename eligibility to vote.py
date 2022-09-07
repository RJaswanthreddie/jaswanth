age=int(input("enter the age: "))
if(age>=18):
    print("eligible to vote")
elif(age>0 and age<18):
    print("not eligible to vote/n",18-age,"years left for eligibility")
else:
    ("print invalid input")

