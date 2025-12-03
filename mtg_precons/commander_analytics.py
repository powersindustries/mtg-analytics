# Name;Mana Cost;Type;Description;Color Identity;Sets;Decks

import re;

commander_count = 52;

color_identity_map = {};
color_identity_array = [0] * 10;
mana_cost_array = [0] * 10;


# Cache list of commander names.
commanders = [];
with open('data/commanderList.csv', mode='r') as file:
    for row in file:
        row_array = row.split(";"); 
        commanders.append(row_array[0].replace("\n", ""));


# Search for the commanders in the database.
with open('data/cardDatabase.csv', mode='r') as file:
    for row in file:
        row_array = row.split(";"); 
        commander = row_array[0];
        for comm in commanders :
            if comm == commander :
                # Color identity data.
                color_identity = row_array[4];

                # Account for colorless.
                if color_identity == "" :
                    color_identity = "C";

                if color_identity in color_identity_map :
                    color_identity_map[color_identity] += 1;
                else :
                    color_identity_map[color_identity] = 1;

                # Mana cost data.
                mana_cost = row_array[1];
                mana_array = re.findall(r'\{(.*?)\}', mana_cost)

                cost = 0;
                for pip in mana_array :
                    if pip.isdigit() :
                        cost += int(pip);
                    else :
                        cost += 1;

                mana_cost_array[cost] += 1;


# Color count calculation.
for key in color_identity_map:
    color_count = len(key);
    color_identity_array[color_count] += color_identity_map[key]; 




# Print findings.
print("Commander mana curve analytics (How much mana you need to cast the commander).");
index = 0;
for cost in mana_cost_array:
    print(str(index) + " mana : " + str(cost) + ", " + str(cost / commander_count * 100) + "%");
    index += 1;
print("\n");


print("Commander color count analytics (How many different colors you need to cast the commander).");
index = 0;
for value in color_identity_array:
    if value > 0:
        print(str(index) + " color : " + str(value) + ", " + str(value / commander_count * 100) + "%");
    index += 1;
print("\n");

print("Commander color pairing analytics (What colors do you need to cast the commander).");
sorted_output = dict(sorted(color_identity_map.items(), key=lambda item: (len(item[0]), item[0])))
for key in sorted_output:
    value = sorted_output[key];
    print(key + ": " + str(value) + ", " + str(value / commander_count * 100) + "%");
