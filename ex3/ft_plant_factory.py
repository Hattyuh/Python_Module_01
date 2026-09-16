class Plant():
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.grow_speed = round(height / age, 1)
        self.growth = 0
        print("Created: ", end="")
        self.show()

    def show(self):
        print(f"{self.name}: {self.height} cm, {self.age} days old")

    def grow(self):
        self.height = round(self.height + self.grow_speed, 1)
        self.growth = round(self.growth + self.grow_speed, 1)
        self.age += 1


def simulate_week(plant: Plant):
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.show()
    print(f"Growth this week: {plant.growth}")


def main():
    rosa = Plant("Rosa", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    subflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    main()
    print("=== End of Program ===")
