from data_manager import DataManager
import json

data_manager = DataManager()

all_card_data = {}
with open("data.json", 'r') as file:
    all_card_data = json.load(file)

# Process cards.
card_names = all_card_data.keys()
for card in card_names:
    card_data = all_card_data[card]
    cost_map = card_data['price_map']

    if cost_map == {}:
        continue

    # Commander.
    legalities = card_data['legalities']
    if 'modern' in legalities and legalities['modern'] == 'Legal':

        identity = card_data['color_identity']

        # Comment/uncomment out the blocks below depending on what type of search you want to do (All identity vs Exact Identity).

        # 1. Total cards, any color identity
        if identity == "":
            data_manager.process_card("COLORLESS", cost_map)
        else:
            # Identity included color.
            for color in identity:
                data_manager.process_card(color, cost_map)

    
        # 2. Identity is exact color.
        # if identity == "":
        #     data_manager.process_card("COLORLESS", cost_map)
        # else:
        #     data_manager.process_card(identity, cost_map)


# Print output.
data_manager.print()