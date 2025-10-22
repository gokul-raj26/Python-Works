a=int(input("enter subject 1:"))
b=int(input("enter subject 2:"))
c=int(input("enter subject 3:"))
d=int(input("enter subject 4:"))
e=int(input("enter subject 5:"))
total=a+b+c+d+e
print("Total:",total)
percentage=total/500*100
print("percentage:",percentage)
if percentage>=80:
    print("Grade:A")
elif percentage>=70 and percentage<=80:
    print("Grade:B")
elif percentage>=60 and percentage<=70:
    print("Grade:C")
elif percentage>=40 and percentage<=60:
    print("Grade:D")
elif percentage<=40:
    print("Grade:E")
else:
    print("invalid grade")
    
    
