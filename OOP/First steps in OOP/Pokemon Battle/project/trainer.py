from project.pokemon import Pokemon

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons: list[Pokemon] = []
    def add_pokemon(self, pokemon: Pokemon):
        poke_details = pokemon.pokemon_details()
        if poke_details not in self.pokemons:
            self.pokemons.append(poke_details)
            return f"Caught {poke_details}"
        else:
            return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        for poke in self.pokemons:
            if poke.split()[0] == pokemon_name:
                self.pokemons.remove(poke)
                return f"You have released {pokemon_name}"
        else:
            return f"Pokemon is not caught"

    def trainer_data(self):
        final_result = f"Pokemon Trainer {self.name}\n"
        final_result += f"Pokemon count {len(self.pokemons)}\n"
        for poke in self.pokemons:
            final_result += f"- {poke}\n"
        return final_result.strip()