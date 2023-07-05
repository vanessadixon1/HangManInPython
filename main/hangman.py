import random
import stages

choices = ["Love", "Cool", "Happiness", "Cat", "Candy"]

index_num = random.randint(0, len(choices) - 1)

random_pick = choices[index_num].lower()

word_to_guess = []

end_of_game = False

count_tries = 7

word_for_checking = ""

for character in range(0, len(random_pick)):
    word_to_guess += "_"
    word_for_checking += "0"

print(stages.logo)

print(f"\n{word_to_guess}")

count = 0

while not end_of_game:
    user_input = input("\npick a single letter:\n").lower()

    if user_input == "":
        print("no response received")
    elif len(user_input) > 1:
        print("You can only select one letter. Please try again!")
    else:

        if user_input not in random_pick and count_tries > 0:
            print(stages.stages[count_tries-1])
            if count_tries == 2:
                print(f"Please try again you have {count_tries - 1} try")
            elif count_tries > 2:
                print(f"Please try again you have {count_tries - 1} tries")
            else:
                print("GAME OVER YOU LOSE!👎🏾")
                end_of_game = True
            count_tries -= 1

        for position in range(len(random_pick)):
            if random_pick[position] == user_input and position == 0:
                word_to_guess[position] = user_input.upper()
                count += 1
            elif random_pick[position] == user_input:
                word_to_guess[position] = user_input.lower()
                count += 1

        if count == len(word_to_guess):
            print("CONGRATULATIONS YOU WON!👏🏾")
            end_of_game = True

        print(word_to_guess)


