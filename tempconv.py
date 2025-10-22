def find_fahrenheit(c):
    f=(c*9/5)+32
    print(f"The given celsius{c}c is converted to fahrenheit :{f:.2f}f")
    
def find_celsius(f):
      c=(f-32)*5/9
      print(f"The given fahrenheit{f}f converted to celsius  : {c:.2f}c")
      
choice=str(input("convert to (celsius or fahrenheit ):")).lower ()

if choice=="fahrenheit":
      a=float(input("enter temperature in celsius:"))
      find_fahrenheit(a)
elif choice=="celsius":
      b=float(input("enter temperature in fahrenheit:"))
      find_celsius(b)
else:
      print("invalid choice")
