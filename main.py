from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("I can walk")

class Snake(Animal):
    def move(self):
        print("I can slither")

Rocky = Dog()
Rocky.move()

Ekans = Snake()
Ekans.move()
