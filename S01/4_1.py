from s1 import Car

class Car2(Car):
    def __init__(self, name, color, product_date, capacity=60):
        super().__init__(name, color, product_date)
        self.capacity = capacity

    def __str__(self):
        return f"{super().__str__()} Capacity: {self.capacity}"
        # return f"Name: {self.name} Color: {self.color} production: {self.product_date} Capacity: {self.capacity}"

c = Car('pride', 'red', 1394)
print(c)
c.test()