class Animal():
    name = ""
    age = 0

    def __init__(self):
        pass

    def speak(self):
        pass


class Cat(Animal):
    def __init__(self):
        pass

class Dog(Animal):
    color = "brown"

def main():
    my_dog = Dog()
    print (my_dog.color, my_dog.breed_type)
    print (my_dog.__dict__)
    my_dog.bark_age()



if __name__ == "__main__":
    main()