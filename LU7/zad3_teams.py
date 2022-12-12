class InvalidParameterError(Exception):
    def __init__(self, name):
        self.name = name
        print(f"Invalid class parameter: {self.name}")


class InvalidAgeError(InvalidParameterError):
    def __init__(self, age):
        super()
        self.age = age
        print(f"Invalid parameter: {self.age}")


class InvalidSoundError(InvalidParameterError):
    def __init__(self, sound):
        super()
        self.sound = sound
        print(f"Invalid parameter: {self.sound}")


class JungleAnimal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

        if type(name) != str:
            raise InvalidParameterError(name)
        if type(age) != int:
            raise InvalidAgeError
        if type(sound) != str:
            raise InvalidSoundError

    def make_sound(self):
        print(f"{self.name} says {self.sound}!")

    def print(self):
        pass

    def daily_task(self):
        pass


class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        super.__init__(name, age, sound)
        if age > 15:
            raise InvalidAgeError(age)
        if sound.count("r") < 2:
            raise InvalidSoundError
        
    def print(self):
        print(f"Jaguar({self.name}, {self.age}, {self.sound})")


