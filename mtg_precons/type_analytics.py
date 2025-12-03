# Name;Mana Cost;Type;Description;Color Identity;Sets;Decks

from dataclasses import dataclass
from typing import List

@dataclass
class Analytics:
    card: List[str]
    count: int 

all_cards = Analytics([], 0);
artifact = Analytics([], 0);
creature = Analytics([], 0);
instant = Analytics([], 0);
sorcery = Analytics([], 0);
enchantment = Analytics([], 0);
equipment = Analytics([], 0);
aura = Analytics([], 0);
fancy_land = Analytics([], 0);

artifact_count = 0;
creature_count = 0;
instant_count = 0;
sorcery_count = 0;
enchantment_count = 0;
equipment_count = 0;
aura_count = 0;
fancy_land_count = 0;


with open('data/cardDatabase.csv', mode='r') as file:

    for row in file:

        row_array = row.split(";"); 

        type = row_array[2];
        count = len(row_array[6].split(","));

        # All Cards.
        if count > all_cards.count :
            all_cards.card.clear();
            all_cards.card.append(row);
            all_cards.count = count;
        elif count == all_cards.count :
            all_cards.card.append(row);


        if "Artifact" in type :
            artifact_count += 1;
            if count > artifact.count :
                artifact.card.clear();
                artifact.card.append(row);
                artifact.count = count;
            elif count == artifact.count :
                artifact.card.append(row);

        if "Creature" in type :
            creature_count += 1;
            if count > creature.count :
                creature.card.clear();
                creature.card.append(row);
                creature.count = count;
            elif count == creature.count :
                creature.card.append(row);

        if "Instant" in type :
            instant_count += 1;
            if count > instant.count :
                instant.card.clear();
                instant.card.append(row);
                instant.count = count;
            elif count == instant.count :
                instant.card.append(row);

        if "Sorcery" in type :
            sorcery_count += 1;
            if count > sorcery.count :
                sorcery.card.clear();
                sorcery.card.append(row);
                sorcery.count = count;
            elif count == sorcery.count :
                sorcery.card.append(row);

        if "Enchantment" in type :
            enchantment_count += 1;
            if count > enchantment.count :
                enchantment.card.clear();
                enchantment.card.append(row);
                enchantment.count = count;
            elif count == enchantment.count :
                enchantment.card.append(row);

        if "Equipment" in type :
            equipment_count += 1;
            if count > equipment.count :
                equipment.card.clear();
                equipment.card.append(row);
                equipment.count = count;
            elif count == equipment.count :
                equipment.card.append(row);

        if "Aura" in type :
            aura_count += 1;
            if count > aura.count :
                aura.card.clear();
                aura.card.append(row);
                aura.count = count;
            elif count == aura.count :
                aura.card.append(row);

        if "Land" in type :
            fancy_land_count += 1;
            if count > fancy_land.count :
                fancy_land.card.clear();
                fancy_land.card.append(row);
                fancy_land.count = count;
            elif count == fancy_land.count :
                fancy_land.card.append(row);




print("All cards, count: " + str(all_cards.count));
print(all_cards.card);
print("\n");

print("Total Artifact count: " + str(artifact_count));
print("Artifacts, count: " + str(artifact.count) + ", \n");
print(artifact.card);
print("\n");

print("Total Creature count: " + str(creature_count));
print("Creature, count: " + str(creature.count) + ", \n");
print(creature.card);
print("\n");

print("Total Instant count: " + str(instant_count));
print("Instant, count: " + str(instant.count) + ", \n");
print(instant.card);
print("\n");

print("Total Sorcery count: " + str(sorcery_count));
print("Sorcery, count: " + str(sorcery.count) + ", \n");
print(sorcery.card);
print("\n");

print("Total Enchantment count: " + str(enchantment_count));
print("Enchantment, count: " + str(enchantment.count) + ", \n");
print(enchantment.card);
print("\n");

print("Total Equipment count: " + str(equipment_count));
print("Equipment, count: " + str(equipment.count) + ", \n");
print(equipment.card);
print("\n");

print("Total Aura count: " + str(aura_count));
print("Aura, count: " + str(aura.count) + ", \n");
print(aura.card);
print("\n");

print("Total Fancy Land count: " + str(fancy_land_count));
print("Fancy Land, count: " + str(fancy_land.count) + ", \n");
print(fancy_land.card);
print("\n");
