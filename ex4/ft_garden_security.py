class SecurePlant():
    """
    Clase de planta que valida altura y edad para evitar valores negativos.
    """
    def __init__(self, name, height, age):
        self.name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height):
        """
        Establece la altura de la planta si es válida.
        """
        if height < 0:
            print(
                f"\nInvalid operation attempted: height {height}cm [REJECTED]"
                "\nSecurity: Negative height rejected"
                )

        else:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, age):
        """
        Establece la edad de la planta si es válida.
        """
        if age < 0:
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days [OK]")

    def get_height(self):
        """
        Devuelve la altura actual de la planta.
        """
        return self._height

    def get_age(self):
        """
        Devuelve la edad actual de la planta.
        """
        return self._age



if __name__ == "__main__":

    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    rose.set_height(-5)
    print(
        f"\nCurrent plant: {rose.name} "
        f"({rose.get_height()}cm, {rose.get_age()} days)"
        )
