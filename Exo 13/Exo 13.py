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


print(create_deck())
