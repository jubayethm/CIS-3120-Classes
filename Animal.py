class Animal:
    def __init__(self, name):
        self.__name = name 
        print("hello, I am", self.__name)

    def talk(self):
        print("hi")

    def eat(self, food):
        print(f"{self.__name} is eating {food}")

    def sleep(self, hours):
        print(f"{self.__name} sleeps for {hours} hours")

    def play(self, toy):
        print(f"{self.__name} is playing with a {toy}")

    def describe(self):
        print(f"{self.__name} is a wonderful animal!")

    def sound(self, noise="default sound"):
        print(f"{self.__name} makes a {noise} sound")

    def eat(self, food):
        print(f"{self.__name} is eating {food}")