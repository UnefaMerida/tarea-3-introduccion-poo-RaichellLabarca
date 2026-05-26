class Car:
    # El método __init__ se llama constructor.
    # self se refiere a la instancia del objeto.
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Un método es una función dentro de una clase.
    def start_engine(self):
        print(f"{self.make} {self.model} ¡El motor arrancó!")

# Creamos una instancia (objeto) de la clase Car
my_car = Car("Vera", "SOCIALISTA", 2021)

# Accedemos a los atributos y métodos del objeto
print(f"Mi MOTO es un {my_car.make} {my_car.model}{my_car.year} .")
my_car.start_engine()
