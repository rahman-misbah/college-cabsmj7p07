class Car:
    def __init__(self, make:str, model:str, year:int) -> None:
        self._make = make
        self._model = model
        self._year = year

    def display_info(self):
        print(f"{self._make} {self._model} {self._year}")

# Instances of Car class
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2022)

# Call display_info()
car1.display_info()
car2.display_info()