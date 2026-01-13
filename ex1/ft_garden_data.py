class Plant:
    """
    Clase que representa una planta con nombre, altura y edad.
    """
    def __init__(self, name, height, age):
        """
        Inicializa una planta con su nombre, altura y edad.
        """
        self.name = name
        self.height = height
        self.age = age


def main():
    """
    Programa principal que crea varias plantas e imprime sus datos.
    """
    print("=== Garden Plant Registry ===")

    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
    print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old")
    print(f"{cactus.name}: {cactus.height}cm, {cactus.age} days old")


if __name__ == "__main__":
    main()
