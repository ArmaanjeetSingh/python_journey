vehicles =  {
    "fortuner": "toyota",
    "swift":"maruti",
    "swift": "maruti suzuki",
    "city": "honda",
    "verna": "hyundai",
    "xuv700": "mahindra",
    "scorpio": "mahindra",
    "endeavour": "ford",
    "creta": "hyundai"
}
# for key in vehicles:
#     print(key,vehicles[key],sep =", ")

vehicles["alto k10"] = "maruti" #index into dictionary to assign values to dictionary
vehicles["ambassdor"] = "maruti"
vehicles["toy"] = "glider"


#upgrade values of dicitonary
vehicles["verna"] = "er5"

#iteraion over dictionary
for key,value in vehicles.items():
    print(key,value,sep=", ")