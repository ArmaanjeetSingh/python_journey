class Vehicle:
    total_rented = 0
    def __init__(self,name,rental_days):
        self.name = name
        self.rental_days = rental_days
        Vehicle.total_rented += 1

    def calculate_rent(self):
        if not self.name :
            return f"Provide vehicle name for renting"

        return f"{self.name} is rented for with {self.rental_days} days"

    @classmethod
    def total_vehicles_rented(cls):
        return f"Total vehicles rented {cls.total_rented}"


class Car(Vehicle):
    def __init__(self,name,rental_days):
        super().__init__(name,rental_days)
        self.rate_per_day = 10

    def calculate_rent(self):
        rent = self.rental_days * self.rate_per_day
        return f"{self.name} x {self.rental_days} = {rent}"


class Bike(Vehicle):
    def __init__(self,name,rental_days):
        super().__init__(name,rental_days)
        self.rate_per_day = 5

    def calculate_rent(self):
        rent = self.rental_days * self.rate_per_day
        return f"{self.name} x {self.rental_days} = {rent}"


class Truck(Vehicle):
    def __init__(self,name,rental_days):
        super().__init__(name,rental_days)
        self.rate_per_day = 25

    def calculate_rent(self):
        rent = self.rental_days * self.rate_per_day
        return f"{self.name} x {self.rental_days} = {rent}"


class VehicleSystem :
    def __init__(self):
        self.vehicles_list = []

    def rent_vehicle(self):
        vehicle_type = input("Enter vehicle type you want to rent ").casefold()
        vehicle_rent_days = int(input("Enter days you want to rent for "))
        if vehicle_type == "car".casefold():
            self.vehicles_list.append(Car(vehicle_type,vehicle_rent_days))
        elif vehicle_type == "bike".casefold():
            self.vehicles_list.append(Bike(vehicle_type,vehicle_rent_days))
        elif vehicle_type == "truck".casefold():
            self.vehicles_list.append(Truck(vehicle_type,vehicle_rent_days))
        else:
            print("Invalid choice")


    def calculate_total_rent(self):
        rent_list = []
        total = 0
        for vehicle in self.vehicles_list:
            rent_list.append(vehicle.calculate_rent())
            print(vehicle.calculate_rent())
        for item in rent_list:
            total += int(''.join(item.split("=")[1]))
        #     total += int(item.split("=")[:1])
        print("Total rent : ",total)


if __name__ == '__main__':
    vs_1 = VehicleSystem()
    vs_1.rent_vehicle()
    vs_1.rent_vehicle()
    vs_1.calculate_total_rent()
    print(vs_1.vehicles_list[0].total_vehicles_rented())
