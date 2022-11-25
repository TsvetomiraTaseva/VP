class Person:
    def __init__(self, first_name, last_name, age, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality

    def print(self):
        print(f"My name is {self.first_name} {self.last_name}. I'm {self.age} years old and I am {self.nationality}.")


class Student(Person):
    def __init__(self, first_name, last_name, age, nationality, university, year_of_study):
        super().__init__(first_name, last_name, age, nationality)
        self.university = university
        self.year_of_study = year_of_study

    def print(self):
        print(f"I'm {self.first_name}. I study in {self.university} for {self.year_of_study} year.")


niko = Person("Nikolai", "Aleksandrov", 20, "bulgarian")
niko1 = Student("Nikolai", "Aleksandrov", 20, "bulgarian", "Technical University", "second")

niko.print()
niko1.print()


class Lecturer(Person):
    def __init__(self, first_name, last_name, age, nationality, university, experience):
        super().__init__(first_name, last_name, age, nationality)
        self.university = university
        self.experience = experience

    def print(self):
        print(f"I have {self.experience} years like a lecturer in {self.university}")


niko2 = Lecturer("Nikolai", "Aleksandrov", 20, "bulgarian", "Technical University", 2)
niko2.print()
