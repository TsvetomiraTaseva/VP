class Animal:
    def __init__(self, name, age, food):
        self.name = name
        self.age = age
        self.food = food

    def make_sound(self):
        pass

    def eat_food(self, quantity):
        pass


class Cat(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)

    def make_sound(self):
        print("Meow!")

    def eat_food(self, quantity):
        if quantity == 0:
            for i in range(4):
                self.make_sound()
            return 0
        elif quantity < 10:
            for k in range(2):
                self.make_sound()
            return 0
        return quantity - 10


class Dog(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)

    def make_sound(self):
        print("Bau!")

    def eat_food(self, quantity, eat_quantity=5):
        if quantity > eat_quantity:
            return quantity - eat_quantity
        return 0


class Duck(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)

    def make_sound(self):
        print("Cvack!")

    def eat_food(self, quantity):
        import random
        number_of_food = random.randint(1, 9)
        if number_of_food > quantity:
            return 0
        else:
            return quantity - number_of_food


class Horse(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)

    def make_sound(self):
        print("I!")

    def eat_food(self, quantity):
        if 30 > quantity > 8:
            return quantity - 8

        elif quantity < 8:
            return 0
        return quantity - 15


dict_food = {"meal": 28, "eggs": 84, "carrots": 46, "grass": 56}

list_animals = [Cat("Djula", 12, "meal"), Dog("Aira", 3, "eggs"), Horse("Kosara", 2, "carrots"),
                Cat("Djesi", 7, "eggs"),
                Dog("Koso", 7, "meal"), Horse("Mila", 4, "grass"), Duck("Lili", 3, "grass"),
                Dog("Suzi", 4, "meal"),
                Duck("Loli", 0, "grass"), Cat("Misha", 9, "eggs")]

for i in list_animals:
    print("=======")
    for x in range(10):
        current_quantity = dict_food[i.food]
        dict_food[i.food] = i.eat_food(current_quantity)
        print(f"{i.name} the {type(i).__name__} just ate {current_quantity - dict_food[i.food]} "
              f"{i.food}, there's {dict_food[i.food]} left")
