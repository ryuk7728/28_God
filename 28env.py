from cards import Cards
import random

class GameEnv:

    def __init__(self):
        
        self.reset()
    
    def reset(self):

        self.cards = Cards.packOf28()
        random.shuffle(self.cards)

        self.player1Cards = self.cards[0:4]
        self.player2Cards = self.cards[4:8]
        self.player3Cards = self.cards[8:12]
        self.player4Cards = self.cards[12:16]

        self.bidding = True

    def step(self,action):

        if self.bidding:

            print("The bidding starts now")

            print("Player 1 cards are:")
            for card in self.player1Cards:
                print(card.identity())

            print("Enter your bid, starting from 14. Max bid is 28")
            self.player1Bid = int(input())
            while self.player1Bid<14 or self.player1Bid>28:
                print("Invalid Bid. Enter your bid, starting from 14. Max bid is 28")
                self.player1Bid = int(input())
            
            self.finalBid = 1


            print("Player 2 cards are:")
            for card in self.player2Cards:
                print(card.identity())
                
            print(f"Enter your bid, greater than {self.player1Bid} and max 28 or pass by entering 0")
            self.player2Bid = int(input())
            while (self.player2Bid!=0 and self.player2Bid<=self.player1Bid) or self.player2Bid>28:
                print(f"Invalid Bid. Enter your bid, greater than {self.player1Bid} and max 28 or pass by entering 0")
                self.player2Bid = int(input())
            
            if self.player2Bid == 0:
                self.player2pass = True
            else:
                self.player2pass = False
                self.finalBid = 2
            
            if not self.player2pass:

                print("Player 3 cards are:")
                for card in self.player3Cards:
                    print(card.identity())
                
                print(f"Enter your bid, greater than {self.player2Bid} and max 28 or pass by entering 0")
                self.player3Bid = int(input())
                while (self.player3Bid!=0 and self.player3Bid<=self.player2Bid) or self.player3Bid>28:
                    print(f"Invalid Bid. Enter your bid, greater than {self.player2Bid} and max 28 or pass by entering 0")
                    self.player3Bid = int(input())
            
                if self.player3Bid == 0:
                    self.player3pass = True
                else:
                    self.player3pass = False
                    self.finalBid = 3

            else:
                self.player3pass = True
                self.player3Bid = 0

            if self.player2pass or (not self.player3pass):

                print("Player 4 cards are:")
                for card in self.player4Cards:
                    print(card.identity())
                
                greater = self.player1Bid
                if not self.player3pass:
                     greater = self.player3Bid


                print(f"Enter your bid, greater than {greater} and max 28 or pass by entering 0")
                self.player4Bid = int(input())
                while (self.player4Bid!=0 and self.player4Bid<=greater) or self.player4Bid>28:
                    print(f"Invalid Bid. Enter your bid, greater than {greater} and max 28 or pass by entering 0")
                    self.player4Bid = int(input())
            
                if self.player4Bid == 0:
                    self.player4pass = True
                else:
                    self.player4pass = False
                    self.finalBid = 4
                
            else:
                self.player4pass = True
                self.player4Bid = 0

            
            bids = [self.player1Bid,self.player2Bid,self.player3Bid,self.player4Bid]
            self.finalBidValue = bids[self.finalBid-1]
            print(f"The bids are: {self.player1Bid},{self.player2Bid},{self.player3Bid},{self.player4Bid}")
            print(f"The final bid is by player {self.finalBid} and the value is {self.finalBidValue}")

            if self.finalBid==1:
                print("Player 1 cards, select your trump card by entering 0/1/2/3")
                for card in self.player1Cards[0:4]:
                    print(card.identity())
                ind = int(input())
                self.playerTrump = self.player1Cards[ind]
                self.player1Cards.pop(ind)
            
            if self.finalBid==2:
                print("Player 2 cards, select your trump card by entering 0/1/2/3")
                for card in self.player2Cards[0:4]:
                    print(card.identity())
                ind = int(input())
                self.playerTrump = self.player2Cards[ind]
                self.player2Cards.pop(ind)

            if self.finalBid==3:
                print("Player 3 cards, select your trump card by entering 0/1/2/3")
                for card in self.player3Cards[0:4]:
                    print(card.identity())
                ind = int(input())
                self.playerTrump = self.player3Cards[ind]
                self.player3Cards.pop(ind)

            if self.finalBid==4:
                print("Player 4 cards, select your trump card by entering 0/1/2/3")
                for card in self.player4Cards[0:4]:
                    print(card.identity())
                ind = int(input())
                self.playerTrump = self.player4Cards[ind]
                self.player4Cards.pop(ind)

            
            playerCards1 = [self.player1Cards.copy(), self.player2Cards.copy(), self.player3Cards.copy()
                            , self.player4Cards.copy()]
            
            
            self.player1Cards.extend(self.cards[16:20])
            self.player2Cards.extend(self.cards[20:24])
            self.player3Cards.extend(self.cards[24:28])
            self.player4Cards.extend(self.cards[28:])

            print("Player 1 cards are:")
            print()
            for card in self.player1Cards:
                    print(card.identity())
            print("Player 2 cards are:")
            print()
            for card in self.player2Cards:
                    print(card.identity())
            print("Player 3 cards are:")
            print()
            for card in self.player3Cards:
                    print(card.identity())
            print("Player 4 cards are:")
            print()
            for card in self.player4Cards:
                    print(card.identity())

            self.players = []

            for i in range(4):
                player = {'cards':playerCards1[i]+self.cards[i*4+16:i*4+20],'isTrump':i==(self.finalBid-1),'team':1 if i % 2 == 0 else 2, 'trump':self.playerTrump if i==(self.finalBid-1) else None}
                self.players.append(player)

            self.playerChance = random.randint(0,3)
            self.catches = []
            self.team1Catches = []

            self.team2Catches = []
            self.team1Points = []
            self.team2Points = []

            self.gameDone = False
            self.trumpReveal = False
            self.bidding = False
            self.catchNumber = 0
        
        
        self.currentCatch = []
        self.currentSuit = ''

        self.trumpSuit = self.playerTrump.suit
        print(f"Trump Suit: {self.trumpSuit}")

        for i in range(4):
            
            print("The cards already played are:")
            for k in self.currentCatch:
                print(k.identity())

            self.playerChance = self.playerChance%4
            print(f"Player {self.playerChance+1}'s chance to play")

            if i==0:

                if self.players[self.playerChance]['isTrump']:

                    if self.trumpReveal:

                        print("Your valid card options are given below, enter the number to choose which card to play:")
                        for j in range(len(self.players[self.playerChance]['cards'])):
                            print(f"{j} : {self.players[self.playerChance]['cards'][j].identity()}")
                        cardNum = int(input("Enter card number"))

                        while cardNum<0 or cardNum> len(self.players[self.playerChance]['cards'])-1:
                            cardNum = int(input(f"Invalid card number, Enter card number from 0 to {len(self.players[self.playerChance]['cards'])-1}"))

                        self.currentCatch.append(self.players[self.playerChance]['cards'][cardNum])
                        self.currentSuit = self.players[self.playerChance]['cards'][cardNum].suit
                        self.players[self.playerChance]['cards'].pop(cardNum)
                        
                        
                        for j in self.players[self.playerChance]['cards']:
                            print(j.identity())
                        print(f"{self.currentCatch[0].identity()}, {self.currentSuit}, {self.playerChance}")

                        self.playerChance+=1


                    else:

                        validCards = []
                        for j in range(len(self.players[self.playerChance]['cards'])):
                            if not self.players[self.playerChance]['cards'][j].suit == self.trumpSuit:
                                validCards.append(self.players[self.playerChance]['cards'][j])
                        

                        print("Your valid card options are given below, enter the number to choose which card to play:")
                        for j in range(len(validCards)):
                            print(f"{j} : {validCards[j].identity()}")
                        cardNum = int(input("Enter card number"))

                        while cardNum<0 or cardNum> len(validCards)-1:
                            cardNum = int(input(f"Invalid card number, Enter card number from 0 to {len(validCards)-1}"))

                        self.currentCatch.append(validCards[cardNum])
                        self.currentSuit = validCards[cardNum].suit
                        self.players[self.playerChance]['cards'].remove(validCards[cardNum])
                        

                        for j in self.players[self.playerChance]['cards']:
                            print(j.identity())
                        print(f"{self.currentCatch[0].identity()}, {self.currentSuit}, {self.playerChance}")

                        self.playerChance+=1
                
                else:

                        print("Your valid card options are given below, enter the number to choose which card to play:")
                        for j in range(len(self.players[self.playerChance]['cards'])):
                            print(f"{j} : {self.players[self.playerChance]['cards'][j].identity()}")
                        cardNum = int(input("Enter card number"))

                        while cardNum<0 or cardNum> len(self.players[self.playerChance]['cards'])-1:
                            cardNum = int(input(f"Invalid card number, Enter card number from 0 to {len(self.players[self.playerChance]['cards'])-1}"))

                        self.currentCatch.append(self.players[self.playerChance]['cards'][cardNum])
                        self.currentSuit = self.players[self.playerChance]['cards'][cardNum].suit
                        self.players[self.playerChance]['cards'].pop(cardNum)
                        

                        for j in self.players[self.playerChance]['cards']:
                            print(j.identity())
                        print(f"{self.currentCatch[0].identity()}, {self.currentSuit}, {self.playerChance}")

                        self.playerChance+=1


                            
                        



                        
                        




        



        



env = GameEnv()
env.step(action=0)