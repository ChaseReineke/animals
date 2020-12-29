class Zoo():
    def __init__(self, name, animals=[]):
        self.name = name
        self.animals = []
    def add_animal(self, animal_name):
        self.animals.append(animal_name)
        return self
    def print_all_animals(self):
        print(f"In {self.name}, we have the following animals: ")
        for animal in self.animals:
            animal.display_info()

class Animal():
    def __init__(self, name, age, health_level, happiness_level):
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level
    def feed_animal(self):
        self.health_level += 10
        self.happiness_level += 10
        return self

class Lion(Animal):
    def __init__(self, name, age, health_level, happiness_level):
        super().__init__(name, age, health_level, happiness_level)
        self.skill = "Claws"
    def display_info(self):
        print(f"{self.name} is at {self.health_level} health level and at {self.happiness_level} happiness level! My special skill is {self.skill}.")
        return self
    def feed_animal(self):
        self.health_level += 20
        self.happiness_level += 10
        return self


class Panda(Animal):
    def __init__(self, name, age, health_level, happiness_level):
        super().__init__(name, age, health_level, happiness_level)
        self.skill = "Bamboo"
    def display_info(self):
        print(f"{self.name} is at {self.health_level} health level and at {self.happiness_level} happiness level! My special skill is {self.skill}.")
        return self
    def feed_animal(self):
        super().feed_animal()
        return self

class PolarBear(Animal):
    def __init__(self, name, age, health_level, happiness_level):
        super().__init__(name, age, health_level, happiness_level)
        self.skill = "Cold"
    def display_info(self):
        print(f"{self.name} is at {self.health_level} health level and at {self.happiness_level} happiness level! My special skill is {self.skill}.")
        return self
    def feed_animal(self):
        super().feed_animal()
        return self

zoo_one = Zoo("Chase's Zoo")

simba = Lion("Simba", 5, 100, 100)
zoo_one.add_animal(simba)
simba.feed_animal().feed_animal().feed_animal()

dragon_warrior = Panda("Dragon Warrior", 2, 30, 30)
zoo_one.add_animal(dragon_warrior)
dragon_warrior.feed_animal().feed_animal().feed_animal().feed_animal().feed_animal()

david = PolarBear("David", 1, 50, 50)
zoo_one.add_animal(david)
david.feed_animal().feed_animal().feed_animal().feed_animal().feed_animal()

naga = PolarBear("Naga", 1, 50, 50)
zoo_one.add_animal(naga)
naga.feed_animal().feed_animal().feed_animal().feed_animal().feed_animal()

zoo_one.print_all_animals()