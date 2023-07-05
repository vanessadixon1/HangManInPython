import random
import stages

choices = ["Love", "Cool", "Happiness", "Cat", "Candy"]

index_num = random.randint(0, len(choices) - 1)

random_pick = choices[index_num].lower()

guess_word = []

end_of_game = False

count_tries = 7

word_for_checking = ""

for character in range(0, len(random_pick)):
    guess_word += "_"
    word_for_checking += "0"

print(stages.logo)

print(f"\n{guess_word}")

count = 0

while not end_of_game:
    user_input = input("\npick a single letter:\n").lower()

    if user_input == "":
        print("no response received")
    elif len(user_input) > 1:
        print("You can only select one letter. Please try again!")
    else:
        user_index = -1

        for index in range(0, len(random_pick)):
            if random_pick[index] == user_input:
                user_index = index

        if user_index == -1 and count_tries > 0:
            print(stages.stages[count_tries - 1])
            if count_tries == 1:
                print("GAME OVER YOU LOSE!👎🏾")
                end_of_game = True
            else:
                if count_tries == 2:
                    print(f"Please try again you have {count_tries - 1} more try")
                else:
                    print(f"Please try again you have {count_tries - 1} more tries")
                count_tries -= 1

        for position in range(len(random_pick)):
            if random_pick[position] == user_input and position == 0:
                guess_word[position] = user_input.upper()
                count += 1
            elif random_pick[position] == user_input:
                guess_word[position] = user_input.lower()
                count += 1

        if count == len(guess_word):
            print("CONGRATULATIONS YOU WON!👏🏾")
            end_of_game = True

        print(guess_word)


