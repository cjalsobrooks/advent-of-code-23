# reads input file, parses out all numerical values, selects first and last number from each line (combination code), sums all combination codes to get final answer

# read input file
file = open(r"1/inputdec1.txt")
lines = file.readlines()

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
number_word = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
codes = []

# parse and add codes to list
for line in lines:
    line_nums = []
    for word in number_word:
        if word in line:
            line = line.replace(word, word + str(number_word[word]) + word)
    entry = list(line)
    for char in entry:
        if char in numbers:
            line_nums.append(char)
    first = line_nums[0]
    last = line_nums[-1]
    code = first + last
    print(line + "=>" + code)
    codes.append(int(code))



# calculate and print sum
sum = 0
for code in codes:
    sum += code

print("The sum of all codes is " + str(sum))