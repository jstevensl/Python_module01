class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def main():
    plants_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Forn", 15, 120),
    ]

    plants = []
    print("=== Plant Factory Output ===")

    for name, height, age in plants_data:
        plant = Plant(name, height, age)
        plants.append(plant)
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")

    print(f"\nTotal plants created: {len(plants)}")


if __name__ == "__main__":
    main()

# La lista de tuplas es inmutable.
# L21 crea un nuevo objeto Plant y lo guarda en la variable plant.
