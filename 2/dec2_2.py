# read input file
file = open(r"2/input.txt")
lines = file.readlines()

TOTAL_IDS = 5050

colors = {'red':12, 'blue':14, 'green':13}
possible_values = [' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ', ' 10 ', ' 11 ', ' 12 ', ' 13 ', ' 14 ', ' 15 ', ' 16 ', ' 17 ', ' 18 ', ' 19 ', ' 20 ']
powers = []

# DICTIONARY: GAME ID: [RED, GREEN, BLUE]
for line in lines:
    line.replace('\\n', '')
    split_id_colors = line.split(':')
    
    split_game_id = split_id_colors[0].split(' ')
    game_id = split_game_id[1]
    
    split_trials = split_id_colors[1].split(';')
    print(split_trials)

    color_highest = {'red':0, 'blue':0, 'green':0}
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
                        if occurences > color_highest[color]:
                            color_highest[color] = occurences
    
    power_calc = 1
    for color in colors:
        power_calc *= color_highest[color]
    powers.append(power_calc)
    
print(sum(powers))

                           
                        
