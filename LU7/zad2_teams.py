class InvalidParameterError(Exception):
    pass


class NutrientError(Exception):
    pass


class InvalidFoodError(Exception):
    pass


class Food:
    def __init__(self, carbs, protein, fats, salt):
        self.carbs = carbs
        self.protein = protein
        self.fats = fats
        self.salt = salt

        if type(self.salt) is not float:
            raise InvalidParameterError
        if type(self.fats) is not float:
            raise InvalidParameterError
        if type(self.carbs) is not float:
            raise InvalidParameterError
        if type(self.protein) is not float:
            raise InvalidParameterError

        if self.fats + self.salt + self.carbs + self.protein > 100:
            raise NutrientError

        if self.salt == 0 and self.fats == 0 and self.carbs == 0 and self.protein == 0:
            raise InvalidFoodError

    def print_label(self):
        print(f"Food: ({self.carbs};{self.protein};{self.fats};{self.salt})")


for i in range(0, 120, 10):
    try:
        food_name = Food(23.4, 22, 275.3, 12.8)
    except InvalidFoodError:
        print("No chance sum of the nutrients = 0")
    except NutrientError:
        print("High nutrient")
    except InvalidParameterError:
        print("Parameter error")
    else:
        food_name.print_label()




