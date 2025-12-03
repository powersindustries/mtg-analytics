import os;

decks_directory = "/path/to/mtg-precon-analysis/data/decks";
search_string = "Command Tower";

output = [];

for filename in os.listdir(decks_directory):
    file_path = os.path.join(decks_directory, filename);
    with open(file_path, "r") as file :
        if search_string not in file.read() :
            output.append(filename);


print(output);
