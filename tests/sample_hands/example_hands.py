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

def get_game2():
        
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
        ("Diamonds", "Jack"),
        ("Diamonds", "Ten"),
        ("Spades", "Nine"),
        ("Clubs", "Queen"),
        ("Spades", "Ace"),
        ("Diamonds", "King"),
        ("Spades", "Eight"),
        ("Clubs", "Ten"),
    ]

    P2 = [
        ("Hearts", "Jack"),
        ("Hearts", "Queen"),
        ("Spades", "King"),
        ("Hearts", "Ace"),
        ("Spades", "Ten"),
        ("Diamonds", "Eight"),
        ("Spades", "Seven"),
        ("Clubs", "Jack"),
    ]

    P3 = [
        ("Spades", "Jack"),
        ("Clubs", "Ace"),
        ("Diamonds", "Seven"),
        ("Hearts", "Seven"),
        ("Hearts", "Ten"),
        ("Hearts", "King"),
        ("Clubs", "Eight"),
        ("Clubs", "Nine"),
    ]

    P4 = [
        ("Diamonds", "Nine"),
        ("Diamonds", "Ace"),
        ("Diamonds", "Queen"),
        ("Spades", "Queen"),
        ("Hearts", "Eight"),
        ("Hearts", "Nine"),
        ("Clubs", "King"),
        ("Clubs", "Seven"),
    ]

    def make_cards(spec):
        return [Cards(suit, rank, *pts_and_order(rank)) for suit, rank in spec]

    return [make_cards(P1), make_cards(P2), make_cards(P3), make_cards(P4)]


def get_game3():
        
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
        ("Clubs", "Jack"),
        ("Clubs", "Nine"),
        ("Clubs", "Ace"),
        ("Clubs", "Queen"),
        ("Hearts", "Nine"),
        ("Hearts", "Eight"),
        ("Hearts", "Seven"),
        ("Diamonds", "Ten"),
    ]

    P2 = [
        ("Spades", "Jack"),
        ("Spades", "Nine"),
        ("Spades", "Queen"),
        ("Clubs", "Ten"),
        ("Clubs", "Seven"),
        ("Diamonds", "King"),
        ("Diamonds", "Seven"),
        ("Hearts", "Ten"),
    ]

    P3 = [
        ("Diamonds", "Jack"),
        ("Diamonds", "Nine"),
        ("Diamonds", "Ace"),
        ("Diamonds", "Queen"),
        ("Spades", "Ten"),
        ("Spades", "Eight"),
        ("Spades", "Seven"),
        ("Clubs", "King"),
    ]

    P4 = [
        ("Hearts", "Jack"),
        ("Hearts", "Ace"),
        ("Hearts", "King"),
        ("Hearts", "Queen"),
        ("Clubs", "Eight"),
        ("Spades", "Ace"),
        ("Spades", "King"),
        ("Diamonds", "Eight"),
    ]

    def make_cards(spec):
        return [Cards(suit, rank, *pts_and_order(rank)) for suit, rank in spec]

    return [make_cards(P1), make_cards(P2), make_cards(P3), make_cards(P4)]

