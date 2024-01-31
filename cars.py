import random
def carSelection():
    cars=["Nissan","Hyundai","Honda","Suzuki","Kia"]
    selectedCar=random.choice(cars)
    print(selectedCar)

def modelYear():
    model=["1998","2001","2005","2010","2012","2022","2024"]
    randomModel=random.choice(model)
    print(randomModel)
    
carSelection()
modelYear()
