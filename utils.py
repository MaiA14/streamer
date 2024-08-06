import base64
import json
import pokedex_pb2

class Utils:
    @staticmethod
    def get_secret(key: str) -> str:
        return base64.b64encode(key.encode('utf-8')).decode('utf-8')

    @staticmethod
    def decode_protobuf_bytes_to_json(protobuf_data: bytes) -> str:
        pokemon = pokedex_pb2.Pokemon()
        pokemon.ParseFromString(protobuf_data)
        pokemon_dict = {
            "number": pokemon.number,
            "name": pokemon.name,
            "type_one": pokemon.type_one,
            "type_two": pokemon.type_two,
            "total": pokemon.total,
            "hit_points": pokemon.hit_points,
            "attack": pokemon.attack,
            "defense": pokemon.defense,
            "special_attack": pokemon.special_attack,
            "special_defense": pokemon.special_defense,
            "speed": pokemon.speed,
            "generation": pokemon.generation,
            "legendary": pokemon.legendary
        }
        return json.dumps(pokemon_dict, indent=2)
