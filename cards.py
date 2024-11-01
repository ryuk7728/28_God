class Cards:
    
    def __init__(self,suit,rank,points):
        self.suit = suit
        self.rank = rank
        self.points = points

    def identity(self):
        return f"{self.rank} of {self.suit}"
    
    @classmethod
    def packOf28(cls):
        
        pack = list([])
        suits = ["Hearts","Clubs","Diamonds","Spades"]
        ranks = ["Seven","Eight","Queen","King","Ten","Ace","Nine","Jack"]

        for suit in suits:
            for rank in ranks:
                point = 0
                if rank == "Ten" or rank == "Ace":
                    point = 1
                if rank == "Nine":
                    point = 2
                if rank == "Jack":
                    point = 3

                card = cls(suit,rank,point)
                pack.append(card)

        return pack



