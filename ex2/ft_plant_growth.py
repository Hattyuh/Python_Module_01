class Plant():
    def __init__(self, name: str, height: float, age: int, grow_speed: float):
        self.name = name
        self.height = height
        self.age = age
        self.grow_speed = grow_speed
        self.growth = 0

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
    rosa = Plant("Rosa", 25, 30, 0.8)
    rosa.show()
    simulate_week(rosa)


if __name__ == "__main__":
    main()
