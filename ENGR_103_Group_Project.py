#######################################################################
# Program Filename: ENGR_103_Group_Project.py
# Authors: Dax Chiavarini, Emery Cole, Leslie Koopmann
# Date: 5/19/2025
# Description: Play Wheel of Fortune and guess your own custom phrases!
# Input: Text file, player name, player game decisions
# Output: User scores, game events, ending winstate, game stats
######################################################################
# TESTING TESTING 123 #

# Pseudocode

# # ask user for text doc
# try:
#     phrase_list = tuple(text_doc)
# except:
#     let user try again

# # convert text doc into a fully capitalized list of phrases
# textdoc = textdoc.upper()
# phrase_list = list(textdoc.split(','))

# # randomly select a phrase for round
# random_phrase = random.choice(phrase_list)
# phrase_list.remove(random_phrase)

# # Begin game loop
# for round in range(3):

# # Begin round loop
# for player in player_list:

# # encrypt phrase into blanks, display to user
# encrypted_phrase = phrase_encrypt(phrase)
# print(encrypted_phrase)

# # Ask player to spin the wheel (press space or something) and randomly pick tile to land on from wheel tile list

# spin_wheel()
# random_tile = random.choice(wheel_tile_list)
# if random_tile = bankrupt or skip turn:
#     if bankrupt:
#         balance = 0
#     skip turn
# else:
#     random_tile = letter_value

# # Give user list of actions to choose from (guess, solve, buy vowel)
# player_action = player_action_input(player_balance)
# if player action is guess:
#     letter_guess = letter_guess_input(letter_list)
#     letter_list.remove(letter_guess)
#     if letter_guess in random phrase:
#         print(f"Yes, we have some {letter_guess}s")
#         encrypted_phrase = phrase_letter_reveal(letter_guess, number_letter_revealed)
#         score += number_letters_revealed*letter_value
#     else:
#         print(f"Ooh, sorry, no {letter_guess}s")
#         break loop
# elif player action is buy vowel:
#     letter_guess = letter_guess_input(vowel_list)
#     player balance -= 250
#     vowel_list.remove(letter_guess)
#     if letter_guess in random phrase:
#         print(f"Yes, we have some {letter_guess}s")
#         encrypted_phrase = phrase_letter_reveal(letter_guess, number_letter_revealed)
#         score += number_letters_revealed*letter_value
#     else:
#         print(f"Ooh, sorry, no {letter_guess}s")
#         break loop
# elif player action is solve:
#     player solve = player_solve_input()
#     if player solve == secret phrase:
#         secret_phrase_reveal(secret_phrase)
#         print("Congrats you won")
#         player balance += score
#         end round

# # If puzzle solved, end round
# if revealed phrase == encrypted phrase:
#     winner balance += earnings
#     end round

# # After all rounds are done, print results
# scoreboard()


import random


# Example error checking function:

# def time_input():
#     while True:
#         while True:
#             time = input("Please enter the length of the simulation in seconds: ")
#             try:
#                 time = int(time)
#                 break
#             except TypeError:
#                 print("ERROR: Input must be a whole number")
#             except ValueError:
#                 print("ERROR: Input must be a whole number")
#             except:
#                 exit()
#         if 1 <= time <= 500:
#             break
#         else:
#             print("ERROR: Input must be between 1 and 500 seconds")
#     return time


def encrypted_phrase_create(fsecret_phrase):

    fencrypted_phrase = []
    for character in fsecret_phrase:
        if character.isalpha() == True:
            fencrypted_phrase.append("_")
        elif character == " ":
            fencrypted_phrase.append(" ")
        elif character == "\'" or character == "-":
            fencrypted_phrase.append(character)

    return fencrypted_phrase


def text_doc_name_input():
    while True:

        text_doc_name = input("Please enter the name of the .txt file you wish to use for phrases (i.e. phrase_list.txt): ")
        try:
            open(text_doc_name)
            break
        except:
            print(f"ERROR: Could not open file named \"{text_doc_name}\". Please make sure the file location is in the Python directory.")

    return text_doc_name


def text_doc_convert(text_doc_name):

    phrase_list = open(text_doc_name)
    phrategory_list = []
    lost_phrases = 0
    try:
        for phrase in phrase_list:
            phrase = phrase.upper()
            phrase = list(phrase.split(", "))
            if len(phrase) != 2:
                x = 1/0
            print(phrase)
            phrategory_list.append(phrase)
    except:
        lost_phrases += 1
    if lost_phrases > 0:
        print(f"{lost_phrases} phrase(s) were discarded due to improper formatting")
    print(phrategory_list)

    return phrategory_list


def main():

    # Gets text_doc from user, convert to capitalized list of phrases
    # text_doc_name = text_doc_name_input()
    # phrase_list = open("phrase_list.txt")
    # phrategory_list = []
    # lost_phrases = 0
    # try:
    #     for phrase in phrase_list:
    #         phrase = phrase.upper()
    #         phrase = list(phrase.split(", "))
    #         print(phrase)
    #         phrategory_list.append(phrase)
    # except:
    #     lost_phrases += 1
    # if lost_phrases > 0:
    #     print(f" {lost_phrases} were discarded due to improper formatting")
    # print(phrategory_list)

    text_doc_name = text_doc_name_input()
    phrategory_list = text_doc_convert(text_doc_name)

    # Picks random phrase out of phrase list
    secret_phrategory = random.choice(phrategory_list)
    phrategory_list.remove(secret_phrategory)
    print(secret_phrategory)

    # Separate category from phrase and store as separate variables
    secret_phrase = secret_phrategory[0]
    category = secret_phrategory[1]
    print(secret_phrase)
    print(category)

    # Encrypts the phrase into blanks
    encrypted_phrase = encrypted_phrase_create(secret_phrase)
    print(encrypted_phrase)

    # Display category and encrypted phrase as string
    print(f"{" ".join(encrypted_phrase)}")
    print(f"Category is {category}")


main()
