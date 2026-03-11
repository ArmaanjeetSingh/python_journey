day = "Monday"
temp = 30
raining = False
if (day == "Saturday" and temp > 27) or not raining:
    print("Go swimming")
else:
    print("learn python")
    
if day == "Saturday" and (temp > 27 or not raining):
    print("Go swimming")
else:
    print("learn python")
    
if day == "Saturday" and temp > 27 or not raining:
    print("Go swimming")
else:
    print("learn python")