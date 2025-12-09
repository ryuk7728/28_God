from src.cards import Cards

def get_special_case1():
    # P1: A hearts
    # P2: J spade
    # P3: Q hearts
    # P4: A diamond
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
    P1 = [("Hearts", "Ace")]
    P2 = [("Spades", "Jack")]
    P3 = [("Hearts", "Queen")]
    P4 = [("Diamonds", "Ace")]
    def make_cards(spec):
        return [Cards(suit, rank, *pts_and_order(rank)) for suit, rank in spec]
    return [make_cards(P1), make_cards(P2), make_cards(P3), make_cards(P4)]

def get_special_case2():
    # A hearts, 9 hearts, K spade, T diamond
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
    P1 = [("Hearts", "Ace")]
    P2 = [("Hearts", "Nine")]
    P3 = [("Spades", "King")]
    P4 = [("Diamonds", "Ten")]
    def make_cards(spec):
        return [Cards(suit, rank, *pts_and_order(rank)) for suit, rank in spec]
    return [make_cards(P1), make_cards(P2), make_cards(P3), make_cards(P4)]

def get_special_case3():
    # 9 hearts, A hearts, 7 diamonds, 8 spade
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
    P1 = [("Hearts", "Nine")]
    P2 = [("Hearts", "Ace")]
    P3 = [("Diamonds", "Seven")]
    P4 = [("Spades", "Eight")]
    def make_cards(spec):
        return [Cards(suit, rank, *pts_and_order(rank)) for suit, rank in spec]
    return [make_cards(P1), make_cards(P2), make_cards(P3), make_cards(P4)]
