import random
import json

class ParkingLot:
    def __init__(self, square_footage, spot_length=8, spot_width=12):
        self.spot_length = spot_length
        self.spot_width = spot_width
        self.total_spots = square_footage // (spot_length * spot_width)
        self.lot = [None] * self.total_spots
        self.parked_cars = {}

    def park(self, car, spot):
        if spot < 0 or spot >= self.total_spots:
            return "Invalid spot number"

        if self.lot[spot] is None:
            self.lot[spot] = car
            self.parked_cars[car.license_plate] = spot
            return f"Car with license plate {car} parked successfully in spot {spot}"
        else:
            return f"Spot {spot} is occupied"

    def map_parked_cars(self):
        return self.parked_cars

class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return self.license_plate

def main():
    parking_lot_size = int(input("Enter parking lot size: "))
    parking_lot = ParkingLot(parking_lot_size) 
    cars = []
    n = int(input("Enter how many cars you want to park."))
    for i in range(0, n):
      cars.append(Car(input("Enter License Plate Number: ")))

    print(cars)

    while cars and None in parking_lot.lot:
        car = random.choice(cars)
        spot = random.randint(0, len(parking_lot.lot) - 1)
        result = parking_lot.park(car, spot)
        
        if result.startswith("Car with"):
            print(result)
            cars.remove(car)
        else:
            print(result + ", trying another spot...")

    mapped_cars = parking_lot.map_parked_cars()
    with open('mapped_cars.json', 'w') as file:
        json.dump(mapped_cars, file)

if __name__ == "__main__":
    main()
