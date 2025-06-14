from Decorators.computer_store.project.computer_types.computer import Computer

class DesktopComputer(Computer):
    @property
    def available_processors(self):
        return {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200
        }

    @property
    def max_ram(self):
        return 64

    # def __str__(self):
    #     return "desktop computer"
    @property
    def name(self):
        return "desktop computer"