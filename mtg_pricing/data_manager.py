import json
from dataclasses import dataclass

@dataclass
class Card:
    name: str
    color_identity: str
    uuids: list[str]
    price_map: dict[str, float]
    legalities: dict[str,str]

class DataManager:
    color_map = {
    # Single Colors
    'B': {'cost': 0.0, 'count': 0},
    'G': {'cost': 0.0, 'count': 0},
    'R': {'cost': 0.0, 'count': 0},
    'U': {'cost': 0.0, 'count': 0},
    'W': {'cost': 0.0, 'count': 0},

    # Two-Color Pairings
    'BG': {'cost': 0.0, 'count': 0},
    'BR': {'cost': 0.0, 'count': 0},
    'BU': {'cost': 0.0, 'count': 0},
    'BW': {'cost': 0.0, 'count': 0},
    'GR': {'cost': 0.0, 'count': 0},
    'GU': {'cost': 0.0, 'count': 0},
    'GW': {'cost': 0.0, 'count': 0},
    'RU': {'cost': 0.0, 'count': 0},
    'RW': {'cost': 0.0, 'count': 0},
    'UW': {'cost': 0.0, 'count': 0},

    # Three-Color Pairings
    'BGR': {'cost': 0.0, 'count': 0},
    'BGU': {'cost': 0.0, 'count': 0},
    'BGW': {'cost': 0.0, 'count': 0},
    'BRU': {'cost': 0.0, 'count': 0},
    'BRW': {'cost': 0.0, 'count': 0},
    'BUW': {'cost': 0.0, 'count': 0},
    'GRU': {'cost': 0.0, 'count': 0},
    'GRW': {'cost': 0.0, 'count': 0},
    'GUW': {'cost': 0.0, 'count': 0},
    'RUW': {'cost': 0.0, 'count': 0},

    # Four-Color Pairings
    'BGRU': {'cost': 0.0, 'count': 0},
    'BGRW': {'cost': 0.0, 'count': 0},
    'BGUW': {'cost': 0.0, 'count': 0},
    'BRUW': {'cost': 0.0, 'count': 0},
    'GRUW': {'cost': 0.0, 'count': 0},

    # Five-Color Pairing
    'BGRUW': {'cost': 0.0, 'count': 0},

    # Colorless
    'COLORLESS': {'cost': 0.0, 'count': 0},
    }

    def process_card(self, identity: str, cost_map: dict[str, float]) :
        # Make sure identity is in color map.
        if identity not in self.color_map: 
            print("Identity doesnt exist with Key: " +  identity)
            return

        # Get min price.
        values = cost_map.values()
        min_price = min(values)

        self.color_map[identity]['cost'] += min_price
        self.color_map[identity]['count'] += 1


    def print(self) :
        keys = self.color_map.keys()

        for key in keys:
            data = self.color_map[key]
            cost = data['cost']
            count = data['count']

            if cost == 0 or count == 0:
                continue

            print("Color: " + key)
            print("Count: " + str(count))
            print("Cost: " + str(cost))
            print("Average: " + str(cost / count))
            print("\n")