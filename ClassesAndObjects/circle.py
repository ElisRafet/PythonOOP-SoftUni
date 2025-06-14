class Circle:
    pi = 3.14
    def __init__(self, r):
        self.radius = r

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        return self.pi * self.radius ** 2

    def get_circumference(self):
        return self.pi * self.radius * 2