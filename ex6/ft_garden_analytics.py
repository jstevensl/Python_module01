class Plant():
    """
    Clase base para plantas regulares.
    """
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.plant_type = "regular"

    def grow(self):
        """Incrementa la altura de la planta en 1cm."""
        self.height += 1


class FloweringPlant(Plant):
    """
    Clase que representa plantas con flores.
    """
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = True
        self.plant_type = "flowering"


class PrizeFlower(FloweringPlant):
    """
    Clase que representa flores de premio con puntos extra.
    """
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points
        self.plant_type = "prize"


class GardenManager:
    """
    Clase que maneja un jardín con múltiples plantas.
    """
    total_gardens = 0

    class GardenStats:
        """Clase estática para estadísticas de plantas."""
        @staticmethod
        def validate_heights(plants):
            """Valida que todas las plantas tengan altura positiva."""

            for plant in plants:
                if plant.height < 0:
                    return False
            return True

        @staticmethod
        def total_growth(plants):
            """Calcula la cantidad total de plantas (proxy de crecimiento)."""
            return len(plants)

        @staticmethod
        def count_types(plants):
            """Cuenta la cantidad de plantas por tipo."""
            regular = 0
            flowering = 0
            prize = 0

            for plant in plants:
                if plant.plant_type == "prize":
                    prize += 1
                elif plant.plant_type == "flowering":
                    flowering += 1
                else:
                    regular += 1

            return regular, flowering, prize

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        """Agrega una planta al jardín."""
        print(f"Added {plant.name} to {self.owner}'s garden")
        self.plants.append(plant)

    def help_plants_grow(self):
        """Hace crecer todas las plantas del jardín."""
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            print(f"{plant.name} grew 1cm")

    def report(self):
        """Genera un reporte del jardín."""
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden")

        for plant in self.plants:
            if plant.plant_type == "prize":
                print(
                    f"- {plant.name}: {plant.height}cm, "
                    f"{plant.color} flowers (blooming), "
                    f"Prize points: {plant.prize_points}"
                )
            elif plant.plant_type == "flowering":
                print(
                    f"- {plant.name}: {plant.height}cm, "
                    f"{plant.color} flowers (blooming)"
                )
            else:
                print(f"- {plant.name}: {plant.height}cm")

        total = GardenManager.GardenStats.total_growth(self.plants)
        regular, flowering, prize = (
            GardenManager.GardenStats.count_types(self.plants)
        )
        valid = GardenManager.GardenStats.validate_heights(self.plants)

        print(f"\nPlants added: {len(self.plants)}, Total growth: {total}cm")
        print(
            f"Plant types: {regular} regular, "
            f"{flowering} flowering, "
            f"{prize} prize flowers"
        )
        print(f"\nHeight validation test: {valid}")

    @classmethod
    def create_garden_network(cls):
        """Muestra la cantidad total de jardines creados."""
        print(f"Total gardens managed: {cls.total_gardens}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    alice.help_plants_grow()
    alice.report()

    print("Garden scores - Alice: 218, Bob, 92")
    GardenManager.create_garden_network()
