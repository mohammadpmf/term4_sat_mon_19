class Dot():
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"({self.x},{self.y})"
    def __add__(self, other):
        return Dot(self.x + other.x,self.y + other.y)
    def __del__(self): # destructor نابود شونده.
        print(f"{self.x} Deleted.")
p1 = Dot(70, 40)
p2 = Dot(-50, 40)
print(p1)
print(p2)
p1 = 'salam'
print(p1)
# __gt__   >
# __lt__   <
# __eq__   ==
# __ne__   !=
# __ge__   >=
# __le__   <=
# __sub__  -
# __mul__  *
# __truediv__ /