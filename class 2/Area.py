print("All of the measurements are measured in cm")
shape = input("Enter the shape that you want to calculate :")
calculate = input("Enter what you want to calculate in that shape :")
if shape == "rectangel" and calculate == "area":
    print("The shape is rectangel")
    print("Calculating the area")
    a = int(input("Enter the legth of one side: "))
    b = int(input("Enter the legth of the other side: "))
    c = a*b
    print("The area of the rectangel in : ",c)
elif shape == "rectangel" and calculate == "perimeter":
    print("The shape is rectangel")
    print("Calculating the perimeter")
    height = int(input("Enter the hight of the rectangel: "))
    length = int(input("Enter the length og the rectangel: "))
    perimeter = height+height+length+length
    print("The perimeter of the recangle is : ",perimeter)
elif shape == "square" and calculate == "area":
    print("The shape is square")
    print("Calculating the area")
    q = int(input("Enter the length of one side: "))
    w = q*q
    print("The area of the sqare is : ",w)
elif shape == "square" and calculate == "perimeter":
    print("The shape is square")
    print("Calculating the perimeter")
    u = int(input("Enter the length of one side: "))
    x = u+u+u+u
    print("The perimeter of the square is : ",x)
elif shape == "circle" and calculate == "area":
    print("The shape is circle")
    print("Calculating the area")
    g = input("What is the length type e.g. Radius or Diameter: ")
    if g == "radius":
        import math
        h = int(input("Enter the radius of the the circle: "))
        t = math.pi * h**2
        print("The area of the circle is : ",t)
    elif g == "diameter":
        import math
        j = int(input("Enter the diameter of the circle: "))
        y = (math.pi * j**2) / 4
        print("The area of the circle is : ",y)
elif shape == "circle" and calculate == "circumference":
    print("The shape is circle")
    print("Calculating the circumfernce")
    z = input("What is the length type e.g. Radius or Diameter: ")  
    if z == "radius":
        import math
        e = int(input("Enter the diameter of the circle: "))
        m = 2 * math.pi * e
        print("The circumfernce of the circle is : ",m)
    elif z == "diameter":
        import math
        k = int(input("Enter the diameter of the circle: "))
        n = math.pi * k
        print("The circumfernce of the circle is : ",n)
elif shape == "triangle" and calculate == "area":
    print("The shape is triangle")
    print("Calculating the area")
    r = int(input("Enter the length of the base: "))
    f = int(input("Enter the height: "))
    v = 0.5 * r * f
    print("The area of the triangle is : ",v)
elif shape == "triangle" and calculate == "perimeter":
    print("The shape is triangle")
    print("Calculating the perimeter")
    i = int(input("Enter the length a side: "))
    o = int(input("Enter the length of anther side: "))
    l = int(input("Enter the length of the last side: "))
    s = i + o + l
    print("The perimeter of the triangle is : ",s)