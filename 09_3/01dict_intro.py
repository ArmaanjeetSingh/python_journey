vehicles =  {
    "fortuner": "toyota",
    "swift": "maruti suzuki",
    "city": "honda",
    "verna": "hyundai",
    "xuv700": "mahindra",
    "scorpio": "mahindra",
    "endeavour": "ford",
    "creta": "hyundai"
}

my_car = vehicles['fortuner']
print(my_car)

commuter = vehicles['scorpio']
print(commuter)

learner = vehicles.get("verna")
print(learner)