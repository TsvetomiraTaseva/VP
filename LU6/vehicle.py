class Vehicle:
    def __init__(self, brand, model, engine_volume, max_speed, kilometers_traveled, max_passengers):
        self.brand = brand
        self.model = model
        self.engine_volume = engine_volume
        self.max_speed = max_speed
        self.kilometers_traveled = kilometers_traveled
        self.max_passengers = max_passengers

    def print_info(self):
        print(f"Vehicle ({self.brand}, {self.model}, {self.engine_volume}, {self.max_speed},"
              f" {self.kilometers_traveled}, {self.max_passengers})")


class Motorbike(Vehicle):
    def __init__(self, brand, model, engine_volume, max_speed, kilometers_traveled, price, car, max_passengers=2):
        super().__init__(brand, model, engine_volume, max_speed, kilometers_traveled, max_passengers)
        self.price = price
        self.car = bool(car)

    def print_info(self):
        print(f"Vehicle ({self.brand}, {self.model}, {self.engine_volume}, {self.max_speed}, "
              f"{self.kilometers_traveled}, {self.max_passengers}, {self.price}, {self.car})")


class Car(Vehicle):
    def __init__(self, brand, model, engine_volume, max_speed, kilometers_traveled, category, fuel, max_passengers = 4):
        super().__init__(brand, model, engine_volume, max_speed, kilometers_traveled, max_passengers)
        self.category = category
        self.fuel = fuel

    def print_info(self):
        print(f"Vehicle ({self.brand}, {self.model}, {self.engine_volume}, {self.max_speed}, "
              f"{self.kilometers_traveled}, {self.max_passengers}, {self.category}, {self.fuel})")


class Bus(Vehicle):
    def __init__(self,brand, model, engine_volume, max_speed, kilometers_traveled,max_passengers,firm,
                 year_of_manufacture ):
        super().__init__(brand, model, engine_volume, max_speed, kilometers_traveled, max_passengers)
        self.firm = firm
        self.year_of_manufacture = year_of_manufacture

    def print_info(self):
        print(f"Vehicle ({self.brand}, {self.model}, {self.engine_volume}, {self.max_speed}, "
              f"{self.kilometers_traveled}, {self.max_passengers}, {self.firm}, {self.year_of_manufacture})")


audi = Vehicle("Audi", "A4", 1.9, 160, 270000, 4)
car = Car("Mercedes-Benz", "E 63 AMG", 5.5, 250, 150000, "euro5", "oil")
mercedes = Car("Mercedes-Benz", "126", 3.0, 230, 155000, "euro6", "gasoline")
yamaha = Motorbike("Yamaha", "YZF", 0.7, 140, 43000, 25600, True)
toyota = Car("Toyota", "Avensis", 3.0, 200, 180000, "euro4", "oil")
bus =Bus("Mercedes-Benz", "258", 3.8, 160, 356500, 6, "NDU", 2022)
golf = Car("Golf", "6", 2.0, 250, 100000, "euro6", "oil")
yamaha11 =(Motorbike("Yamaha", "123", 0.8, 180, 25000, 24600, False))
bus2 = Bus("Bus", "2", 3.0, 170, 24500, 5, "NDO", 2015)

audi.print_info()
car.print_info()
mercedes.print_info()
yamaha.print_info()
toyota.print_info()
bus.print_info()
golf.print_info()
yamaha11.print_info()
bus2.print_info()


