from cards import Cards
import random
import numpy as np

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

    def printCards(self,cards):
        for card in cards:
                print(card.identity())
        
        print("\n")
    
    def callBid(self,min,max):

        bid = int(input())
        while (bid !=0 and bid < min) or bid > max:
                print(f"Invalid Bid. Enter your bid, greater than {min} and max {max} or pass by entering 0")
                bid = int(input())
        return bid

    def passCheck(self,bid,final,num):

            if bid == 0:
                passCond = True
            else:
                passCond = False
                final = num
            
            return passCond,final


    def step(self,action):

        if self.bidding:

            print("The bidding starts now \n\n")
            print("Player 1 cards are: \n")
            self.printCards(self.player1Cards)

            print("Enter your bid, starting from 14. Max bid is 23")
            self.player1Bid = int(input())
            while self.player1Bid<14 or self.player1Bid>23:
                print("Invalid Bid. Enter your bid, starting from 14. Max bid is 23")
                self.player1Bid = int(input())
            
            self.finalBid = 1

            print("Player 2 cards are:")
            self.printCards(self.player2Cards)
                
            print(f"Enter your bid, greater than {self.player1Bid} and max 23 or pass by entering 0")
            self.player2Bid = self.callBid(self.player1Bid,23)
            self.player2pass,self.finalBid = self.passCheck(self.player2Bid,self.finalBid,2)
            
            print("Player 3 cards are:")
            self.printCards(self.player3Cards)
            bidMax = 0

            if not self.player2pass:
                    bidMax = self.player2Bid
            else:
                    bidMax = max(self.player1Bid,19)

            print(f"Enter your bid, greater than {bidMax} and max 23 or pass by entering 0")
            self.player3Bid = self.callBid(bidMax,23)
            self.player3pass,self.finalBid = self.passCheck(self.player3Bid,self.finalBid,3)

            self.player4Bid = 0

            bids = [self.player1Bid,self.player2Bid,self.player3Bid,self.player4Bid]
            if self.finalBid==2:
                greater = max(bids[self.finalBid-1],19)
            else:
                greater = bids[self.finalBid-1]

            print("Player 4 cards are:")
            self.printCards(self.player4Cards)
                

            print(f"Enter your bid, greater than {greater} and max 23 or pass by entering 0")
            self.player4Bid = self.callBid(greater,23)
            
            if not self.player4Bid == 0:
                    self.finalBid = 4
            
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

            self.round1Bid = self.finalBid
            self.round1BidValue = self.finalBidValue

            print("Player 1 cards are:")
            self.printCards(self.player1Cards)
            
            if self.round1Bid==1:
                         print((self.playerTrump).identity())
                    
            
            print(f"Enter your bid, greater than {23} and max 28 or pass by entering 0")
            self.player1Bid = int(input())
            while (self.player1Bid!=0 and self.player1Bid<=23) or self.player1Bid>28:
                print(f"Invalid Bid. Enter your bid, greater than {23} and max 28 or pass by entering 0")
                self.player1Bid = int(input())

            print("Player 2 cards are:")
            self.printCards(self.player2Cards)

            if self.round1Bid==2:
                         print((self.playerTrump).identity())        
            
            maxBid = max(self.player1Bid,23)

            print(f"Enter your bid, greater than {maxBid} and max 28 or pass by entering 0") 
            self.player2Bid = int(input())
            while (self.player2Bid!=0 and self.player2Bid<=maxBid) or self.player2Bid>28:
                print(f"Invalid Bid. Enter your bid, greater than {maxBid} and max 28 or pass by entering 0")
                self.player2Bid = int(input())
                

            print("Player 3 cards are:")
            self.printCards(self.player3Cards)
            
            if self.round1Bid==3:
                         print((self.playerTrump).identity())
            
            maxBid = max(self.player1Bid,self.player2Bid,23)

            print(f"Enter your bid, greater than {maxBid} and max 28 or pass by entering 0")
            self.player3Bid = int(input())
            while (self.player3Bid!=0 and self.player3Bid<=maxBid) or self.player3Bid>28:
                print(f"Invalid Bid. Enter your bid, greater than {maxBid} and max 28 or pass by entering 0")
                self.player3Bid = int(input())
            
            print("Player 4 cards are:")
            self.printCards(self.player4Cards)

            if self.round1Bid==4:
                         print((self.playerTrump).identity())        

            maxBid = max(self.player1Bid,self.player2Bid,self.player3Bid,23)

            print(f"Enter your bid, greater than {maxBid} and max 28 or pass by entering 0")
            self.player4Bid = int(input())
            while (self.player4Bid!=0 and self.player4Bid<=maxBid) or self.player4Bid>28:
                print(f"Invalid Bid. Enter your bid, greater than {maxBid} and max 28 or pass by entering 0")
                self.player4Bid = int(input())
            
            bids = [self.player1Bid,self.player2Bid,self.player3Bid,self.player4Bid]
            self.finalBidValue = max(bids)
            self.finalBid = np.argmax(bids)+1 

            if self.finalBidValue != 0 :
                print(f"The bids are: {self.player1Bid},{self.player2Bid},{self.player3Bid},{self.player4Bid}")
                print(f"The final bid is by player {self.finalBid} and the value is {self.finalBidValue}")
                

                if self.round1Bid == 1:
                    self.player1Cards.append(self.playerTrump)

                if self.round1Bid == 2:
                    self.player2Cards.append(self.playerTrump)

                if self.round1Bid == 3:
                    self.player3Cards.append(self.playerTrump)

                if self.round1Bid == 4:
                    self.player4Cards.append(self.playerTrump)
                
                if self.finalBid==1:
                    print("Player 1 cards, select your trump card by entering 0/1/2/3...")
                    count = 0
                    for card in self.player1Cards:
                        print(f"{count} :",card.identity())
                        count+=1
                    ind = int(input())
                    self.playerTrump = self.player1Cards[ind]
                    self.player1Cards.pop(ind)
                
                if self.finalBid==2:
                    print("Player 2 cards, select your trump card by entering 0/1/2/3...")
                    count = 0
                    for card in self.player2Cards:
                        print(f"{count} :",card.identity())
                        count+=1
                    ind = int(input())
                    self.playerTrump = self.player2Cards[ind]
                    self.player2Cards.pop(ind)
                
                if self.finalBid==3:
                    print("Player 3 cards, select your trump card by entering 0/1/2/3...")
                    count = 0
                    for card in self.player3Cards:
                        print(f"{count} :",card.identity())
                        count+=1
                    ind = int(input())
                    self.playerTrump = self.player3Cards[ind]
                    self.player3Cards.pop(ind)

                if self.finalBid==4:
                    print("Player 4 cards, select your trump card by entering 0/1/2/3...")
                    count = 0
                    for card in self.player4Cards:
                        print(f"{count} :",card.identity())
                        count+=1
                    ind = int(input())
                    self.playerTrump = self.player4Cards[ind]
                    self.player4Cards.pop(ind)
                
                print("Player 1 cards:")
                self.printCards(self.player1Cards)

                print("Player 2 cards:")
                self.printCards(self.player2Cards)

                print("Player 3 cards:")
                self.printCards(self.player3Cards)

                print("Player 4 cards:")
                self.printCards(self.player4Cards)

            else:
                self.finalBid = self.round1Bid
                self.finalBidValue = self.round1BidValue
                print(f"No further bids have been placed, the final bid is by player {self.finalBid} and the value is {self.finalBidValue}")

            

        #     self.players = []

        #     for i in range(4):
        #         player = {'cards':playerCards1[i]+self.cards[i*4+16:i*4+20],'isTrump':i==(self.finalBid-1),'team':1 if i % 2 == 0 else 2, 'trump':self.playerTrump if i==(self.finalBid-1) else None}
        #         self.players.append(player)

        #     self.playerChance = random.randint(0,3)
        #     self.catches = []
        #     self.team1Catches = []

        #     self.team2Catches = []
        #     self.team1Points = []
        #     self.team2Points = []

        #     self.gameDone = False
        #     self.trumpReveal = False
        #     self.bidding = False
        #     self.catchNumber = 0
        
        
        # self.currentCatch = []
        # self.currentSuit = ''

        # self.trumpSuit = self.playerTrump.suit
        # print(f"Trump Suit: {self.trumpSuit}")

        # for i in range(4):
            
        #     print("The cards already played are:")
        #     for k in self.currentCatch:
        #         print(k.identity())

        #     self.playerChance = self.playerChance%4
        #     print(f"Player {self.playerChance+1}'s chance to play")

        #     if i==0:

        #         if self.players[self.playerChance]['isTrump']:

        #             if self.trumpReveal:

        #                 print("Your valid card options are given below, enter the number to choose which card to play:")
        #                 for j in range(len(self.players[self.playerChance]['cards'])):
        #                     print(f"{j} : {self.players[self.playerChance]['cards'][j].identity()}")
        #                 cardNum = int(input("Enter card number"))

        #                 while cardNum<0 or cardNum> len(self.players[self.playerChance]['cards'])-1:
        #                     cardNum = int(input(f"Invalid card number, Enter card number from 0 to {len(self.players[self.playerChance]['cards'])-1}"))

        #                 self.currentCatch.append(self.players[self.playerChance]['cards'][cardNum])
        #                 self.currentSuit = self.players[self.playerChance]['cards'][cardNum].suit
        #                 self.players[self.playerChance]['cards'].pop(cardNum)
                        
                        
        #                 for j in self.players[self.playerChance]['cards']:
        #                     print(j.identity())
        #                 print(f"{self.currentCatch[0].identity()}, {self.currentSuit}, {self.playerChance}")

        #                 self.playerChance+=1


        #             else:

        #                 validCards = []
        #                 for j in range(len(self.players[self.playerChance]['cards'])):
        #                     if not self.players[self.playerChance]['cards'][j].suit == self.trumpSuit:
        #                         validCards.append(self.players[self.playerChance]['cards'][j])
                        

        #                 print("Your valid card options are given below, enter the number to choose which card to play:")
        #                 for j in range(len(validCards)):
        #                     print(f"{j} : {validCards[j].identity()}")
        #                 cardNum = int(input("Enter card number"))

        #                 while cardNum<0 or cardNum> len(validCards)-1:
        #                     cardNum = int(input(f"Invalid card number, Enter card number from 0 to {len(validCards)-1}"))

        #                 self.currentCatch.append(validCards[cardNum])
        #                 self.currentSuit = validCards[cardNum].suit
        #                 self.players[self.playerChance]['cards'].remove(validCards[cardNum])
                        

        #                 for j in self.players[self.playerChance]['cards']:
        #                     print(j.identity())
        #                 print(f"{self.currentCatch[0].identity()}, {self.currentSuit}, {self.playerChance}")

        #                 self.playerChance+=1
                
        #         else:

        #                 print("Your valid card options are given below, enter the number to choose which card to play:")
        #                 for j in range(len(self.players[self.playerChance]['cards'])):
        #                     print(f"{j} : {self.players[self.playerChance]['cards'][j].identity()}")
        #                 cardNum = int(input("Enter card number"))

        #                 while cardNum<0 or cardNum> len(self.players[self.playerChance]['cards'])-1:
        #                     cardNum = int(input(f"Invalid card number, Enter card number from 0 to {len(self.players[self.playerChance]['cards'])-1}"))

        #                 self.currentCatch.append(self.players[self.playerChance]['cards'][cardNum])
        #                 self.currentSuit = self.players[self.playerChance]['cards'][cardNum].suit
        #                 self.players[self.playerChance]['cards'].pop(cardNum)
                        

        #                 for j in self.players[self.playerChance]['cards']:
        #                     print(j.identity())
        #                 print(f"{self.currentCatch[0].identity()}, {self.currentSuit}, {self.playerChance}")

        #                 self.playerChance+=1


                            
                        



                        
                        




        



        



env = GameEnv()
env.step(action=0)