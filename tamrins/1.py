class Car():
    def __init__(self, name, color, product_date):
        self.name = name
        self.color = color
        self.product_date = product_date
    
    def __str__(self):
        return f"Name: {self.name} Color: {self.color} production: {self.product_date}"
    
car1 = Car("Pride", "white", 1396)
car2 = Car("Pride", "Black", 1399)
print(car1)
print(car2)
"Name: Pride Color: white production: 1396"
"Name: Pride Color: black production: 1399"
