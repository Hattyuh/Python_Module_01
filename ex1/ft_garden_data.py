class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height} cm, {self.age} days old")


def main() -> None:
    rosa = Plant("Rosa", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    rosa.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    main()
    print("=== End of Program ===")
