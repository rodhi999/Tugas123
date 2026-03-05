class Vehicle:
    def __init__(self, brand, model):
        if not isinstance(brand, str) or not isinstance(model, str):
            raise TypeError("Brand dan model harus berupa string!")
        
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"The {self.brand} {self.model} is driving.")


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        
        if not isinstance(doors, int):
            raise TypeError("Jumlah pintu harus angka!")
        if doors <= 0:
            raise ValueError("Jumlah pintu harus lebih dari 0!")
        
        self.doors = doors

    def honk(self):
        print("Beep! Beep!")


class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        
        if not isinstance(load_capacity, (int, float)):
            raise TypeError("Load capacity harus angka!")
        if load_capacity <= 0:
            raise ValueError("Load capacity harus lebih dari 0!")
        
        self.load_capacity = load_capacity

    def load(self, weight):
        if weight > self.load_capacity:
            raise ValueError("Muatan melebihi kapasitas!")
        print(f"Loaded {weight} kg.")


def main():
    try:
        my_car = Car("Toyota", "Corolla", 4)
        my_truck = Truck("Ford", "F-150", 1000)

        my_car.drive()
        my_car.honk()

        my_truck.drive()
        my_truck.load(900)  

    except Exception as e:
        print("Terjadi kesalahan:", e)


if __name__ == "__main__":
    main()