import random


def create_deck():
    """
    Cree un deck de 52 cartes (ordonnes)
    :return: Liste de 52 cartes
    """
    deck = []
    color = ["♥", "♦", "♣", "♠"]
    value = ["J", "Q", "K"]
    for i in range(10):
        value.append(str(i+1))

    for col in color:
        for val in value:
            deck.append(val + col)

    return deck


def deck_shuffler(deck):
    """
    Mélange un deck
    :param deck: Deck à mélanger
    :return: Deck mélangé
    """
    random.shuffle(deck)
    return deck


def ask_number_of_player():
    """
    Demande le nombre de joueur de la partie de poker
    :return: Le nombre de joueur
    """
    num_of_player = input("Combien de joueur ? ")
    while int(num_of_player) not in range(2, 7):
        num_of_player = input("Le nombre de joueur doit être compris entre 2 et 6.\nEntrer un nombre de joueur entre 2 et 6 : ")
    return num_of_player


def deal(deck, num_of_player):
    """
    Distribue 2 cartes à chaque joueur
    :param deck: Le deck utilisé ce tour-ci
    :param num_of_player: Le nombre de joueur
    :return: Une liste des mains des joueurs, donc une liste de listes de deux cartes.
    """
    players_new_hand = []
    for player in range(int(num_of_player)):
        hand = []
        for i in range(2):
            hand.append(deck[0])
            deck.pop(0)
        players_new_hand.append(hand)
    return deck, players_new_hand


def flop(deck, current_turn, tapis_card):
    """
    Fonction qui sert les cartes sur la table selon le tour actuel. On brûle une carte d'abord puis on en brûle une ou trois.
    :param deck: Le deck
    :param current_turn: Le tour actuel. 1 = flop de 3 cartes. 2 et 3 = flop d'une carte
    :param tapis_card: Les cartes actuellement sorties
    :return: L'état actuel du deck, le tour qui a été incrémenté de 1, les cartes actuellement sorties
    """
    game_deck.pop(0)
    if current_turn == 1:
        for i in range(3):
            tapis_card.append(deck[0])
            deck.pop(0)
    else:
        tapis_card.append(deck[0])
        deck.pop(0)
    current_turn += 1
    return deck, current_turn, tapis_card




if __name__ == "__main__":
    nb_de_joueur = ask_number_of_player()
    game_deck = deck_shuffler(create_deck())
    game_deck, players_hand = deal(game_deck, nb_de_joueur)
    turn = 1
    cards = []
    print(game_deck)
    while turn < 4:
        game_deck, turn, cards = flop(game_deck, turn, cards)
        print(game_deck)
        print(cards)
