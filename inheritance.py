class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor


class Apple(Fruit):
    pass


class Grape(Fruit):
    pass

# instance
granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")

# print the attribute values
print(granny_smith.color)