class Plant:
    """
    Clase base para cualquier planta.
    """
    def __init__(self, name, height, age):
        """
        Inicializa una planta con atributos comunes.
        """
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """
    Clase que representa una flor.
    """
    def __init__(self, name, height, age, color):
        """
        Inicializa una flor con su color.
        """
        super().__init__(name, height, age)
        self.color = color

    def describe(self):
        """
        Muestra la información de la flor.
        """
        print(
            f"\n{self.name} (Flower): {self.height}cm, "
            f"{self.age} days, {self.color} color"
        )

    def bloom(self):
        """
        Simula que la flor está floreciendo.
        """
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """
    Clase que representa un árbol.
    """
    def __init__(self, name, height, age, trunk_diameter):
        """
        Inicializa un árbol con el diámetro del tronco.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def describe(self):
        """
        Muestra la información del árbol.
        """
        print(
            f"\n{self.name} (Tree): {self.height}cm, "
            f"{self.age} days, {self.trunk_diameter}cm diameter"
        )

    def produce_shade(self):
        """
        Calcula y muestra la sombra que produce el árbol.
        """
        shade_area = self.trunk_diameter * 1.56
        print(f"{self.name} provides {int(shade_area)} square meters of shade")


class Vegetable(Plant):
    """
    Clase que representa una planta comestible.
    """
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """
        Inicializa una verdura con su temporada de cosecha
        y valor nutricional.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def describe(self):
        """
        Muestra la información de la verdura.
        """
        print(
            f"\n{self.name} (Vegetable): {self.height}cm, "
            f"{self.age} days, {self.harvest_season} harvest"
        )

    def show_nutrition(self):
        """
        Muestra el valor nutricional de la verdura.
        """
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    """
    Punto de entrada principal del programa.
    """
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    lily = Flower("Lily", 40, 20, "white")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 600, 2000, 40)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 30, 70, "autumn", "vitamin A")

    rose.describe()
    rose.bloom()

    oak.describe()
    oak.produce_shade()

    tomato.describe()
    tomato.show_nutrition()
