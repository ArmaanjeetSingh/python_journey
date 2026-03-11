menu = [
    ["egg","bacon"],
    ["egg","sausage","bacon"],
    ["egg","spam"],
    ["egg","spam","bacon"],
    ["spam","spam","sausage","egg"],
    ["spam","bacon","sausage","egg"],
    ["spam","bacon","sausage","egg","tomato"]
]

for meal in menu:
    for index in range(len(meal)-1,-1,-1):
        if meal[index] == "spam":
            del meal[index]
            
    print(", ".join(meal))