# Name;Mana Cost;Type;Description;Color Identity;Sets;Decks

card_count = 2638;


# Overall colors regardless of being mono or multi colored.
red_overall = 0;
green_overall = 0;
blue_overall = 0;
black_overall = 0;
white_overall = 0;
colorless_overall = 0;

# Mono colored
red = 0;
green = 0;
blue = 0;
black = 0;
white = 0;

# duel colored
wu = 0;
rw = 0;
bu = 0;
bg = 0;
gr = 0;
ur = 0;
bw = 0;
br = 0;
gw = 0;
ug = 0;

# tri colored
wbg = 0;
guw = 0;
wub = 0;
ubr = 0;
urw = 0;
brg = 0;
rgw = 0;
rwb = 0;
bgu = 0;
gur = 0;

# 5 Color
wubrg = 0;


def contains_colors(identity, color_array):
    return (len(identity) == len(color_array) and set(color_array).issubset(set(identity)));

def get_printable_percentage(color_count):
    return str(color_count / card_count * 100);


with open('data/cardDatabase.csv', mode='r') as file:

    for row in file:

        row_array = row.split(";"); 

        color_identity = row_array[4];


        # Colorless check.
        mana_string = row_array[1];
        mana_no_brackets = mana_string.replace("{", "").replace("}", "").replace("/", "");
        single_mana_no_brackets = ''.join(sorted(set([char for char in mana_string if char.isalpha()])))

        if len(color_identity) == 0 or len(single_mana_no_brackets) == 0 :
            colorless_overall += 1;
            continue;


        # Multi-colored search -> First part that includes color.
        if "R" in color_identity :
            red_overall += 1;
        if "G" in color_identity :
            green_overall += 1;
        if "U" in color_identity :
            blue_overall += 1;
        if "B" in color_identity :
            black_overall += 1;
        if "W" in color_identity :
            white_overall += 1;


        # Mono-Colored search        
        if "R" == color_identity :
            red += 1;
            continue;
        if "G" == color_identity :
            green += 1;
            continue;
        if "U" == color_identity :
            blue += 1;
            continue;
        if "B" == color_identity :
            black += 1;
            continue;
        if "W" == color_identity :
            white += 1;
            continue;

        # Duel-colored search        
        if contains_colors(color_identity, ["W","U"]) :
            wu += 1;
            continue;
        if contains_colors(color_identity, ["B","R"]) :
            br += 1;
            continue;
        if contains_colors(color_identity, ["G","R"]) :
            gr += 1;
            continue;
        if contains_colors(color_identity, ["G","W"]) :
            gw += 1;
            continue;
        if contains_colors(color_identity, ["B","W"]) :
            bw += 1;
            continue;
        if contains_colors(color_identity, ["U","R"]) :
            ur += 1;
            continue;
        if contains_colors(color_identity, ["B","G"]) :
            bg += 1;
            continue;
        if contains_colors(color_identity, ["R","W"]) :
            rw += 1;
            continue;
        if contains_colors(color_identity, ["U","G"]) :
            ug += 1;
            continue;
        if contains_colors(color_identity, ["B","U"]) :
            bu += 1;
            continue;

        # tri colored
        if contains_colors(color_identity, ["W","B","G"]) :
            wbg += 1;
            continue;
        if contains_colors(color_identity, ["G","U","W"]) :
            guw += 1;
            continue;
        if contains_colors(color_identity, ["W","U","B"]) :
            wub += 1;
            continue;
        if contains_colors(color_identity, ["U","B","R"]) :
            ubr += 1;
            continue;
        if contains_colors(color_identity, ["U","R","W"]) :
            urw += 1;
            continue;
        if contains_colors(color_identity, ["B","R","G"]) :
            brg += 1;
            continue;
        if contains_colors(color_identity, ["R","G","W"]) :
            rgw += 1;
            continue;
        if contains_colors(color_identity, ["R","W","B"]) :
            rwb += 1;
            continue;
        if contains_colors(color_identity, ["B","G","U"]) :
            bgu += 1;
            continue;
        if contains_colors(color_identity, ["G","U","R"]) :
            gur += 1;
            continue;

        # 5 Color
        if contains_colors(color_identity, ["W","U","B","R","G"]) :
            wubrg += 1;
            continue;

        print("\n");
        print("You shouldnt be able to get here!!");
        print(color_identity);



# ----------------------------------------------------
# ----------------------------------------------------
# ----------------------------------------------------
# ----------------------------------------------------

# Multi-colored search -> First part that includes color.
print("----------------------------------------------------");
print("Output for colors regardless of color pairing. Percentages are relative.");
print("----------------------------------------------------");
overall_count = red_overall + green_overall + blue_overall + black_overall + white_overall;

print("Red Overall " + str(red_overall) + ", or " + str(red_overall / overall_count * 100) + "%");
print("Green Overall " + str(green_overall) + ", or " + str(green_overall / overall_count * 100) + "%");
print("Blue Overall " + str(blue_overall) + ", or " + str(blue_overall / overall_count * 100) + "%");
print("Black Overall " + str(black_overall) + ", or " + str(black_overall / overall_count * 100) + "%");
print("White Overall " + str(white_overall) + ", or " + str(white_overall / overall_count * 100) + "%");



# ----------------------------------------------------
# ----------------------------------------------------
# ----------------------------------------------------
# ----------------------------------------------------
# Mono colored count.

print("\n");
print("----------------------------------------------------");
print("Mono-colored percentages. How many cards are mono color?");
print("----------------------------------------------------");

print("Colorless Overall " + str(colorless_overall) + ", or " + str(colorless_overall / overall_count * 100) + "%");

print("red " + str(red) + ", or " + get_printable_percentage(red) + "%");
print("green " + str(green) + ", or " + get_printable_percentage(green) + "%");
print("blue " + str(blue) + ", or " + get_printable_percentage(blue) + "%");
print("black " + str(black) + ", or " + get_printable_percentage(black) + "%");
print("white " + str(white) + ", or " + get_printable_percentage(white) + "%");

print("\n");
print("----------------------------------------------------");
print("Two-colored pairing percentages. How many cards are duel color.");
print("----------------------------------------------------");

print("wu " + str(wu) + ", or " + get_printable_percentage(wu) + "%");
print("rw " + str(rw) + ", or " + get_printable_percentage(rw) + "%");
print("bu " + str(bu) + ", or " + get_printable_percentage(bu) + "%");
print("bg " + str(bg) + ", or " + get_printable_percentage(bg) + "%");
print("gr " + str(gr) + ", or " + get_printable_percentage(gr) + "%");
print("ur " + str(ur) + ", or " + get_printable_percentage(ur) + "%");
print("bw " + str(bw) + ", or " + get_printable_percentage(bw) + "%");
print("br " + str(br) + ", or " + get_printable_percentage(br) + "%");
print("gw " + str(gw) + ", or " + get_printable_percentage(gw) + "%");
print("ug " + str(ug) + ", or " + get_printable_percentage(ug) + "%");

print("\n");
print("----------------------------------------------------");
print("Three-colored pairing percentages.");
print("----------------------------------------------------");

print("wbg " + str(wbg) + ", or " + get_printable_percentage(wbg) + "%");
print("guw " + str(guw) + ", or " + get_printable_percentage(guw) + "%");
print("wub " + str(wub) + ", or " + get_printable_percentage(wub) + "%");
print("ubr " + str(ubr) + ", or " + get_printable_percentage(ubr) + "%");
print("urw " + str(urw) + ", or " + get_printable_percentage(urw) + "%");
print("brg " + str(brg) + ", or " + get_printable_percentage(brg) + "%");
print("rgw " + str(rgw) + ", or " + get_printable_percentage(rgw) + "%");
print("rwb " + str(rwb) + ", or " + get_printable_percentage(rwb) + "%");
print("bgu " + str(bgu) + ", or " + get_printable_percentage(bgu) + "%");
print("gur " + str(gur) + ", or " + get_printable_percentage(gur) + "%");

print("\n");
print("----------------------------------------------------");
print("Five-colored pairing percentages.");
print("----------------------------------------------------");
print("wubrg " + str(wubrg) + ", or " + get_printable_percentage(wubrg) + "%");
