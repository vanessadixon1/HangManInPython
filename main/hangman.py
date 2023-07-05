import random
import stages

choices = ["Love", "Cool", "Happiness", "Cat", "Candy"]

index_num = random.randint(0, len(choices) - 1)

random_pick = choices[index_num]

word_to_guess = []

end_of_game = False

count_tries = 7

word_for_checking = ""

for character in range(0, len(random_pick)):
    word_to_guess += "_"
    word_for_checking += "0"

print(stages.logo)

print(f"\n{word_to_guess}")

while not end_of_game:
    user_input = input("\npick a single letter:\n").lower()
    user_input_count = random_pick.lower().count(user_input)
    user_input_index = random_pick.lower().find(user_input)

    if len(user_input) > 1:
        print("You can only select one letter. Please try again!")
    else:
        print(stages.stages[count_tries - 1])
        if user_input_index == -1 and count_tries > 0:
            print(user_input_index)
            if count_tries == 1:
                print("GAME OVER YOU LOSE!👎🏾")
                end_of_game = True
            else:
                print(f"Please try again you have {count_tries - 1}")
                count_tries -= 1

        while user_input_count > 0:
            if user_input_index == 0:
                user_input = user_input.upper()
            word_to_guess[user_input_index] = user_input
            random_pick = random_pick.replace(user_input, "0", 1)
            user_input_count -= 1
            user_input_index = random_pick.lower().find(user_input)
            print(word_to_guess)

        if random_pick == word_for_checking:
            print("CONGRATULATIONS YOU WON!👏🏾")
            end_of_game = True
