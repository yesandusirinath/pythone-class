print("Electricity bill")
units = int(input("Enter the amount of units: "))
price = units
surcharge = 0
if units <100 :        # decides what should be the price per unit
    per_unit = 5
if units >101 <300 :
    per_unit = 7              
if units > 300 :
    per_unit = 10
if units == 100 :
    per_unit = 5    
if units == 101 :
    per_unit = 7    
if units == 300:
    per_unit = 7    
total = price * per_unit  # what is the full price
amount = total  
if units > 1500:          
    surcharge = amount * 0.08          #find what is the extra charge
    applys = "Yes"
else :
    applys = "No"    
Final_price = surcharge + total        #calculate the extar charge
print(f""" 
=================================Bill=================================
      
      How many units                                {units}
      What is the price per unit                    {per_unit}
      Price without the surcharge                   {total}
      Dose a sucharge of 8% applys                  {applys}
      How much is surcharge                         {surcharge}
       
      The total                                     {Final_price}

======================================================================
""")                 # print the final bill