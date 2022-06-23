class Animal:
    # Constructor: weight und height sind Merkmale von Animal die an die Klasse übergeben werden
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    # Method in der Klasse erstellen: muss immer self in der Klammer haben
    def jump(self):
        print("It jumps")


def main():

    # ein Object dog erstellen der in der Animal Klasse ist
    dog = Animal(10, 0.5)
    print(dog.height)
    print(dog.weight)
    dog.jump

    # Object cat in Animal Klasse
    cat = Animal(3, 0.3)
    print(cat.height)
    cat.jump


if __name__ == "__main__":
    main()
