class Animal:
    def fazer_som(self):
        print("Som genérico de animal.")

class Cachorro(Animal):
    def fazer_som(self):
        print("Au au!")

class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

animal1 = Cachorro()
animal2 = Gato()

animal1.fazer_som()
animal2.fazer_som()
