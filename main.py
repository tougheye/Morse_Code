import csv

def main():
    # read the morse code translator table from csv file and save in a dictionary
    with open('morse_code.csv') as csvfile:
        morselist = list(csv.reader(csvfile, delimiter=','))
        eng_string = dict([(morselist[i][0], morselist[i][1]) for i in range(0, (len(morselist) - 1))])

    game_on = True  # while loop to keep playing the game

    while game_on:
        user_string = input('Please enter your string in English using only letters and numbers (to end the game, '
                            'use space+Enter): ').upper()
        # check if the user wants to end the game
        if user_string == " ":
            print('Bye! I hope you will use Morse Codes in your everyday communications.')
            game_on = False
        # if the user does want to play, the for loop will keep the game going
        else:
            morse_translate = ""
            for letter in user_string:
                morse_translate += eng_string[letter]
            print(morse_translate)

if __name__ == '__main__':
    main()