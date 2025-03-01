class Cow:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.milk = 0

    def feed(self):

        self.milk += 1
        print(f"{self.name} : {self.milk} .")

    def milk_cow(self):
        """."""
        if self.milk > 0:
            print(f"Доим {self.name}. {self.milk} .")
            self.milk = 0
        else:
            print(f"{self.name} .")


class Farmer:
    def __init__(self, name):
        self.name = name
        self.cows = []

    def add_cow(self, cow):

        self.cows.append(cow)
        print(f"{cow.name} .")

    def feed_all_cows(self):

        for cow in self.cows:
            cow.feed()

    def milk_all_cows(self):

        for cow in self.cows:
            cow.milk_cow()



farmer = Farmer("Иван")

cow1 = Cow("Милка", 3)
cow2 = Cow("Зорька", 4)

farmer.add_cow(cow1)
farmer.add_cow(cow2)


farmer.feed_all_cows()


farmer.milk_all_cows()
