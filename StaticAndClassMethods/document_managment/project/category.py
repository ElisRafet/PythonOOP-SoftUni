class Category:
    def __init__(self, id_: int, name):
        self.id = id_
        self.name = name

    def edit(self, new_name):
        self.name = new_name

    def __repr__(self):
        return f"Category {self.id}: {self.name}"