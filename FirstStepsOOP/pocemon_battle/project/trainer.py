from typing import List
from project.pokemon import Pokemon

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f'Caught {pokemon.pokemon_details()}'
        return f'This pokemon is already caught'

    def release_pokemon(self, pokemon_name):
        pokemon_to_release = next((p for p in self.pokemons if p.name == pokemon_name), None)
        if pokemon_to_release:
            self.pokemons.remove(pokemon_to_release)
            return f'You have released {pokemon_name}'
        return f'"Pokemon is not caught'

    def trainer_data(self):
        result = [f'Pokemon Trainer {self.name}', f'Pokemon count {len(self.pokemons)}']
        for p in self.pokemons:
            result.append(f"- {p.pokemon_details()}")
        return "\n".join(result)
