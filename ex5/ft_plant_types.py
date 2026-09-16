class Plant():
    def __init__(self, name: str, _height: float, _age: int):
        self.name = name
        self._height = _height
        self._age = _age
        self.grow_speed = round(_height / _age, 1)
        self.growth = 0
        self.show_creation()

    def show(self):
        print(f"{self.name}: {self._height} cm, {self._age} days old")

    def show_creation(self):
        print("Plant created: ", end="")
        self.show()

    def show_current_state(self):
        print("Current state: ", end="")
        self.show()

    def grow(self):
        self._height = round(self._height + self.grow_speed, 1)
        self.growth = round(self.growth + self.grow_speed, 1)
        self._age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"{self.name}: Success, height updated {new_height}")
        self.show_current_state()

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"{self.name}: Success, age updated {new_age}")
        self.show_current_state()


def simulate_week(plant: Plant):
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.show()
    print(f"Growth this week: {plant.growth}")


def main():
    rosa = Plant("Rosa", 25.0, 30)
    rosa.set_age(5)
    rosa.show_current_state()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    main()
    print("=== End of Program ===")
