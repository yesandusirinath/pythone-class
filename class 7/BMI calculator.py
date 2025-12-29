print ("BMI Calculator")
height_in_meters = 0
hight_measuring = input("What is the unit that you know you hight in: ")
if hight_measuring == "cm" or "Cm" or "CM" or "cM":
    height = int(input(f"What is your hight in {hight_measuring}: "))
    height_in_meters = height/100
elif hight_measuring == "feet" or "foot" or "foots" or "feets" or "ft":
    print ("foot and inches taken separately e.g. 6,1 is 6 foot 1 inches")
    feet = int(input("What is you height in foot: "))
    inches = int(input("What is you height in inches: "))
    feet_in_inches = feet*12
    actuval_hight_in_inches = feet_in_inches + inches
    height_in_meters = actuval_hight_in_inches/39.3701    
else:
    height_in_meters = int(input("What is your height in meters: "))    
weight_in_kg = 0    
weight_measuring = input("What is the unit that you measure your weight in: ")
if weight_measuring == "Kg" or "KG" or "kG" or "kg":
    weight_in_kg = int(input("What is you weight in kg: "))
elif weight_measuring == "Lbs" or "LBs" or "lBs" or "lbs" or "LbS" or "LBS" or "lBS" or "lbS" or "pounds":
    lbs = int(input("What is your weight in lbs: "))
    weight_in_kg = lbs/2.20462
BMI_height = height_in_meters * height_in_meters
BMI = weight_in_kg / BMI_height
print(f"Your BMI is {BMI}")
if BMI <= 18.5:
    print("You are Underweight")
elif BMI > 18.5 and BMI <= 24.9:
    print("Healthy Weight")
elif BMI >24.9 and BMI <= 29.9:
    print("Overweight")     
else:
    print("Obese")      