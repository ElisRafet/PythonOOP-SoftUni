from Decorators.computer_store.project.computer_types.computer import Computer

class Laptop(Computer):
    @property
    def available_processors(self):
        return {
            "AMD Ryzen 7 5700G": 500,
            "Intel Core i5-12600K": 600,
            "Apple M1 Max": 1800
        }

    @property
    def max_ram(self):
        return 128

    # def __str__(self):
    #     return "laptop"
    @property
    def name(self):
        return "laptop"