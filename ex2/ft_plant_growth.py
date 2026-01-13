class Plant():
    def __init__(self, name_plant, height_plant, age_plant):
        self.name_plant = name_plant
        self.height_plant = height_plant
        self.age_plant = age_plant

    def grow(self, cm):
        self.height_plant += cm

    def age(self, days):
        self.age_plant += days

    def get_info(self):
        return (
            f"{self.name_plant}: {self.height_plant}, "
            f"{self.age_plant} days old"
        )


def main():

    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print("=== Day 1 ===")
    print(rose.get_info())
    print(sunflower.get_info())
    print(cactus.get_info())

    rose.grow(6)
    rose.age(6)
    sunflower.grow(10)
    sunflower.age(6)
    cactus.grow(2)
    cactus.age(6)

    print("=== Day 7 ===")
    print(rose.get_info())
    print(f"Growth this week: +{rose.height_plant - 25}cm")
    print(sunflower.get_info())
    print(f"Growth this week: +{sunflower.height_plant - 80}cm")
    print(cactus.get_info())
    print(f"Growth this week: +{cactus.height_plant - 15}cm")


if __name__ == "__main__":
    main()
