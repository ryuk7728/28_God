from src.cards import Cards


def get_game1():

    ranks = ["Seven", "Eight", "Queen", "King", "Ten", "Ace", "Nine", "Jack"]

    def pts_and_order(rank):
        points = 0
        if rank in ("Ten", "Ace"):
            points = 1
        elif rank == "Nine":
            points = 2
        elif rank == "Jack":
            points = 3
        order = ranks.index(rank)
        return points, order


    P1 = [
        ("Hearts", "Jack"),
        ("Hearts", "Ace"), 
        ("Hearts", "King"),
        ("Diamonds", "Seven"),
        ("Hearts", "Ten"),
        ("Hearts", "Queen"),
        ("Diamonds", "Jack"),
        ("Diamonds", "Ten"),
    ]

    P2 = [
        ("Hearts", "Nine"),
        ("Clubs", "Ten"),
        ("Clubs", "Ace"),
        ("Spades", "Ten"),
        ("Clubs", "Jack"),
        ("Hearts", "Eight"),
        ("Hearts", "Seven"),
        ("Diamonds", "Nine"),
    ]

    P3 = [
        ("Spades", "King"),
        ("Spades", "Eight"),
        ("Spades", "Queen"),
        ("Spades", "Seven"),
        ("Spades", "Jack"),
        ("Spades", "Ace"),
        ("Spades", "Nine"),
        ("Clubs", "Queen"),
    ]

    P4 = [
        ("Diamonds", "Eight"),
        ("Clubs", "King"),
        ("Clubs", "Eight"),
        ("Diamonds", "King"),
        ("Diamonds", "Ace"),
        ("Diamonds", "Queen"),
        ("Clubs", "Nine"),
        ("Clubs", "Seven"),
    ]

    def make_cards(spec):
        return [Cards(suit, rank, *pts_and_order(rank)) for suit, rank in spec]

    return [make_cards(P1), make_cards(P2), make_cards(P3), make_cards(P4)]

