import math
print("select a shape to calculate its area:")
print("1.Rectangle")
print("2.Square")
print("3.Circle")
print("4.Triangle")
choice=int(input("Enter your choice(1-4):"))
if choice==1:
    try:
        length=float(input("Enter the length of rectangle:"))
        width=float(input("Enter the width of the rectangle:"))
        area=length*width
        print(f"The area of rectangle is{area:.2f}")
    except Value:
        print ("invalid input,please enter a numeric value for length and width")


elif choice==2:
    try:
        side=float(input("Enter the side length of square:"))
        area=side*side
        print(f"The area of square is{area:.2f}")
    except ValueError:
        print("invalid input,please enter a numeric value for side length")


elif choice==3:
    try:
        radius=float(input("Enter the radius of circle:"))
        area=math.pi*(radius**2)
        print(f"The area of circle is {area:.2f}")
    except ValueError:
        print("invalid input,please enter a numeric value for radius")


elif choice==4:
    try:
        base=float(input("Enter the base length of triangle:"))
        height=float(input("Enter the height of the triangle:"))
        area=0.5*base*height
        print(f"The area of triangle is{area:.2f}")
    except:
        print("invalid input,please enter a numeric value for base and height")
        

else:
    print("invalid choice")
        
