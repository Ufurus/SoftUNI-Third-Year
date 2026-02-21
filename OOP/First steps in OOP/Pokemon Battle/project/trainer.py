from project.pokemon import Pokemon

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons: list[Pokemon] = []
    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        pokemon_to_release = next((p for p in self.pokemons if p.name == pokemon_name), None)
        if pokemon_to_release:
            self.pokemons.remove(pokemon_to_release)
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self) -> str:
        final_result = [f"Pokemon trainer {self.name}",
                        f"Pokemon count {len(self.pokemons)}"]
        for poke in self.pokemons:
            final_result.append(f"- {poke.pokemon_details()}")

        return '\n'.join(final_result)