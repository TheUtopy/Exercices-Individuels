def remove_matches(matches_to_remove, number_of_matches):
    number_of_matches -= matches_to_remove
    return number_of_matches

def how_many_matches_to_remove():
    matches_to_remove = int(input("How many matches do you want to remove ? (between 1 and 6) "))
    while matches_to_remove not in [1, 2, 3, 4, 5, 6]:
        matches_to_remove = int(input("Incorrect number of matches. Select an integer between 1 and 6 : "))
    return matches_to_remove

def victory(number_of_matches):
    if number_of_matches == 0:
        return "Victory !"
    elif number_of_matches < 0:
        return "Defeat ..."
    else:
        return True

def victory_prompt(current_player, number_of_matches):
    if number_of_matches == 0:
        return current_player + " win the game !"
    elif number_of_matches < 0:
        return current_player + " lose ... What a loser !"

def change_player(current_player):
    if current_player == "Player 1":
        return "Player 2"
    else:
        return "Player 1"

def game():
    number_of_matches = 50
    number_of_player = ask_number_of_player()
    if number_of_player == 1:
        while victory(number_of_matches) == True:
            print(number_of_matches)
            matches_to_remove = how_many_matches_to_remove()
            number_of_matches = remove_matches(matches_to_remove, number_of_matches)
        else :
            print(victory(number_of_matches))
    else:
        current_player = "Player 1"
        while victory(number_of_matches) == True:
            if number_of_matches != 50:
                current_player = change_player(current_player)
            print(number_of_matches)
            print(current_player)
            matches_to_remove = how_many_matches_to_remove()
            number_of_matches = remove_matches(matches_to_remove, number_of_matches)
        else:
            print(victory_prompt(current_player, number_of_matches))

def ask_number_of_player():
    number_of_player = int(input("How many player ? (1 or 2) "))
    while number_of_player not in [1, 2]:
        number_of_player = int(input("Incorrect number of player. Choose 1 or 2 : "))
    return number_of_player

game()
