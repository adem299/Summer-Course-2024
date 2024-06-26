#!/usr/bin/env python
# coding: utf-8

# In[4]:


def miles_per_gallon():
    total_miles = 0
    total_gallons = 0
    
    while True:
        gallons_used = float(input("Enter the gallons used (-1 to end): "))
        
        if gallons_used == -1:
            break
        
        miles_driven = float(input("Enter the miles driven: "))
        
        miles_per_gallon_tank = miles_driven / gallons_used
        print(f"The miles/gallon for this tank was {miles_per_gallon_tank:.6f}")
        
        total_miles += miles_driven
        total_gallons += gallons_used
    
    if total_gallons != 0:
        overall_miles_per_gallon = total_miles / total_gallons
        print(f"The overall average miles/gallon was {overall_miles_per_gallon:.6f}")
    else:
        print("No data entered.")

miles_per_gallon()


# In[ ]:




