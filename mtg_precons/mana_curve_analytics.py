# Name;Mana Cost;Type;Description;Color Identity;Sets;Decks

import re;

output_array = [0] * 15;

with open('data/cardDatabase.csv', mode='r') as file:
    for row in file:
        row_array = row.split(";"); 

        type = row_array[2];

        if "Land" in type or "Plane" in type or "Phenomenon" in type or type == "" :
            continue;

        mana_cost = row_array[1];
        if mana_cost == "" :
            continue;

        mana_array = re.findall(r'\{(.*?)\}', mana_cost)

        cost = 0;
        for pip in mana_array :
            if pip.isdigit() :
               cost += int(pip);
            else :
               cost += 1;

        output_array[cost] += 1; 


index = 0;
for cost in output_array :
    print(str(index) + " mana: " + str(cost));
    index += 1;
