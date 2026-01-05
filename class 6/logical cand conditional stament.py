m = int(input("Enetr maths mark: "))
b = int(input("Enetr bio mark: "))
cs = int(input("Enetr cs mark: "))
total = b + m + cs
per = total/300 *100
if per>=90 and per<=100:
    print("Grade A")
elif per>=80 and per<90:
    print("Grade B")    
elif per>=70 and per<80:
    print("Grade C")
elif per>=60 and per<70:
    print("Grade D")                   
elif per>=50 and per<60:
    print("Grade E")     
else:
    print("Failed!!")    