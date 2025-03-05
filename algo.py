class CarService:
    def __init__(self, car_type):
        self.car_type = car_type


class MotoCycle(CarService):
    def __init__(self):
        super().__init__("MotoCycle")


class Truck(CarService):
    def __init__(self):
        super().__init__("Truck")


class Bus(CarService):
    def __init__(self):
        super().__init__("Bus")


class Taxi(CarService):
    def __init__(self):
        super().__init__("Taxi")


class CarFactory:
    @staticmethod
    def get_car(car_type):
        car_classes = {
            "MotoCycle": MotoCycle,
            "Truck": Truck,
            "Bus": Bus,
            "Taxi": Taxi,
        }
        car_class = car_classes.get(car_type)
        if car_class:
            return car_class()
        raise ValueError(f"Unknown car type: {car_type}")


car = CarFactory.get_car("Truck")
print(car.car_type)
