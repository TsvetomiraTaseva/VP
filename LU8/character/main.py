from errors import *


all_names_characters = []
all_weapons = []
all_items = []
characters = []


class Menu:
    def print_menu(self):
        print("1. Create a new character")
        print("2. Create a weapon for the character")
        print("3. Create an item for the character")
        print("4. Show all the characters that we are created")
        print("5. Delete a character")
        print("6. Exit")

    def command_create_character(self, name, sex, ch_class, weapon = None, new_item = None):
        if weapon != 0 or new_item != 0:
            raise InvalidCharacterClass
        return name, sex, ch_class, weapon, new_item

    def create_a_new_weapon(self, name, attack):
        return f"Name: {name} with {attack} points."

    def create_an_item(self, name, durability = 100):
        return f"Name: {name} with {durability} durability."


    def run(self):
        # infinite menu loop
        while True:
            self.print_menu()
            # print the menu
            # ...

            # ask the user to choose a command
            choice = input("Choose an item from the menu: \n> ")

            # catch errors
            try:
                # process the user's choice
                if choice == "1":
                    # ask the user to input the necessary command parameters
                    name = input("Enter the character name (alpha-numeric): ")
                    sex = input("Enter female or male: ")
                    ch_class = input("Enter a character class: ")
                    if name in all_names_characters:
                        raise CharacterExists("This name is already used.")
                    elif len(name) < 4 or name.isdigit():
                        raise InvalidDataFormat("Must be not included digits in the name")

                    all_names_characters.append(name)
                    print(all_names_characters)
                    character = self.command_create_character(name, sex, ch_class)
                    characters.append(character)

                    continue
                # !weapon само ако съществува даден герой!
                elif choice == "2":
                    name = input("Enter the character name: ")
                    if name in all_names_characters:
                        name_weapon = input("Enter name weapon: ")
                        attack_points = int(input("Enter attack points: "))
                        if attack_points < 0:
                            raise InvalidCommand("Attack must be positive")
                        all_weapons.append(name_weapon)
                        print(f"The character {name} will use the weapon {name_weapon}")
                        continue
                elif choice == "3":
                    name = input("Enter the character name: ")
                    if name in all_names_characters:
                        name_item = input("Enter the name of the new item")
                        all_items.append(name_item)
                        print(all_items)
                    else:
                        raise CharacterNotFound("The character does not exist")
                    continue
                elif choice == "4":
                    print(f"{characters} \n")
                    continue
                elif choice == "5":
                    pass
                    # ne uspqh da se setq kak da iztriq opredelen geroi
                elif choice == "6":
                    break
                    # ...
                else:
                    raise InvalidCommand("Error: Invalid choice")
            except Exception as ex:
                print(f"Error: {str(ex)}")

            print()


if __name__ == '__main__':
    menu = Menu()
    menu.run()