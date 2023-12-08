# read input file
file = open(r"2/input.txt")
lines = file.readlines()

TOTAL_IDS = 5050

colors = {'red':12, 'blue':14, 'green':13}
possible_values = [' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ', ' 10 ', ' 11 ', ' 12 ', ' 13 ', ' 14 ', ' 15 ', ' 16 ', ' 17 ', ' 18 ', ' 19 ', ' 20 ']
impossible_ids = []

# DICTIONARY: GAME ID: [RED, GREEN, BLUE]
for line in lines:
    line.replace('\\n', '')
    split_id_colors = line.split(':')
    
    split_game_id = split_id_colors[0].split(' ')
    game_id = split_game_id[1]
    
    split_trials = split_id_colors[1].split(';')
    print(split_trials)

    for trial in split_trials:
        for color in colors:
            color_index = trial.find(color)
            if color_index != -1:
                for value in possible_values:
                    search = -1
                    if color_index - 4 < 0:
                        search = trial.rfind(value, trial.find(color) - 3, trial.find(color))
                    else:
                        search = trial.rfind(value, trial.find(color) - 4, trial.find(color))
                    if  search != -1:
                        occurences = int(value)
                        if occurences > colors.get(color):
                            impossible_ids.append(int(game_id))

impossible_ids = list(set(impossible_ids))
total_impossible = sum(impossible_ids)
possible = TOTAL_IDS - total_impossible
print(possible)
