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
        while (bid !=0 and bid <= min) or bid > max:
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
    
    def selectCard(self,cards,option=0,curInd=[]):
        
        if option == 0:
             
            ind = 0
            count = 0
            for card in cards:
                print(f"{count} :",card.identity())
                count+=1

            min = 0
            max = count
            ind = int(input())

            while ind>max or ind<min:
                print(f"Invalid Input. Enter your the number from {min}-{max}")
                ind = int(input())
            return ind

        else:
             count = 0
             for card in cards:
                  if count in curInd:
                       print(f"{count} :",card.identity())
                  count+=1
            
             ind = int(input())
             while not(ind in curInd):
                print(f"Invalid Input. Enter your the number from {curInd}")
                ind = int(input())
             return ind
             
    
    
    def allTrump(self,cards,suit):

        for card in cards:
            if card.suit != suit:
                 break
        else:
             return True
        return False
    
    def validCards(self,cards,currentSuit,trumpSuit):
         
         curSuitInd = []
         trumpSuitInd = []
         count = 0


         for card in cards:
              if card.suit == currentSuit:
                   curSuitInd.append(count)
              if card.suit == trumpSuit:
                   trumpSuitInd.append(count)
              count+=1

         return curSuitInd,trumpSuitInd

    def selectTrumpCard(self, playerNumber, playerCards):

        print(f"Player {playerNumber} cards, select your trump card by entering 0/1/2/3..")
        ind = self.selectCard(playerCards)
        self.playerTrump = playerCards[ind]
        playerCards.pop(ind)

    def extendCards(self):

        self.player1Cards.extend(self.cards[16:20])
        self.player2Cards.extend(self.cards[20:24])
        self.player3Cards.extend(self.cards[24:28])
        self.player4Cards.extend(self.cards[28:])
    
    def performBidding(self, startBid, maxBid):
         
        bids = []
        for i, playerCards in enumerate([self.player1Cards, self.player2Cards, self.player3Cards, self.player4Cards], start=1):
            print(f"Player {i} cards are:")
            self.printCards(playerCards)
            
            if self.round1Bid == i:
                print((self.playerTrump).identity())
            
            maxCurrentBid = max([bid for bid in bids if bid != 0] + [startBid]) 
            print(f"Enter your bid, greater than {maxCurrentBid} and max {maxBid}, or pass by entering 0")
            bid = self.callBid(maxCurrentBid, maxBid)
            bids.append(bid)
        return bids
    
    def selectValidCard(self,validCards,id="0",init="0",ind=[]):

        print(f"{id} Your valid card options are given below, enter the number to choose which card to play:")
        
        if init == "0":
            cardNum = self.selectCard(validCards)
        else:
            cardNum = self.selectCard(validCards,1,ind)
        
        if init=="2":
             if(self.players[self.playerChance]['cards'][cardNum].suit == self.trumpSuit) and self.currentSuit != self.trumpSuit:
                self.trumpPlayed = True
                self.trumpIndice[ind[0]] = 1

        self.currentCatch.append(validCards[cardNum])
        if init == "0":
            self.currentSuit = validCards[cardNum].suit
        self.players[self.playerChance]['cards'].remove(validCards[cardNum])


        for j in self.players[self.playerChance]['cards']:
            print(j.identity())
        print("\n\n")
        print(f"{self.currentCatch[0].identity()}, {self.currentSuit}, {self.playerChance}")

        self.playerChance+=1

         
    

    def step(self,action):

        if self.bidding:
            
            self.bidding = False
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

            if self.finalBid == 1:
                self.selectTrumpCard(1, self.player1Cards)
            elif self.finalBid == 2:
                self.selectTrumpCard(2, self.player2Cards)
            elif self.finalBid == 3:
                self.selectTrumpCard(3, self.player3Cards)
            elif self.finalBid == 4:
                self.selectTrumpCard(4, self.player4Cards)
                 
            self.extendCards()
            self.round1Bid = self.finalBid
            self.round1BidValue = self.finalBidValue

            # Start the next round of bidding
            bids = self.performBidding(23, 28)
            self.player1Bid, self.player2Bid, self.player3Bid, self.player4Bid = bids
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
                
                if self.finalBid == 1:
                    self.selectTrumpCard(1, self.player1Cards)
                elif self.finalBid == 2:
                    self.selectTrumpCard(2, self.player2Cards)
                elif self.finalBid == 3:
                    self.selectTrumpCard(3, self.player3Cards)
                elif self.finalBid == 4:
                    self.selectTrumpCard(4, self.player4Cards)

            else:
                self.finalBid = self.round1Bid
                self.finalBidValue = self.round1BidValue
                print(f"No further bids have been placed, the final bid is by player {self.finalBid} and the value is {self.finalBidValue}")
            
# To test all trumps condition:
        # self.testCards =  Cards.packOfSuit()
        # self.playerTrump = self.testCards[0]
        # self.player1Cards = self.testCards[1:8]
        # self.player2Cards = self.testCards[8:16]
        # self.player3Cards = self.testCards[16:24]
        # self.player4Cards = self.testCards[24:32]
        
        # self.playerCards1 = [self.player1Cards,self.player2Cards,self.player3Cards,self.player4Cards]
        # self.finalBid = 1



        self.playerCards1 = [self.player1Cards,self.player2Cards,self.player3Cards,self.player4Cards]

        self.players = []

        #Initialising new dictionary for players, 'cards' holds the respective cards, 'isTrump' indicates whether the player called, 'team' is 0, if player 1 or player 3, else team is 1, 'trump' holds the trump card if the player called, else holds None
        for i in range(4):
                player = {'cards':self.playerCards1[i],'isTrump':i==(self.finalBid-1),'team':1 if i % 2 == 0 else 2, 'trump':self.playerTrump if i==(self.finalBid-1) else None}
                self.players.append(player)

        # self.playerChance = random.randint(0,3)
        self.playerChance = 0
        self.catches = []
        self.team1Catches = []

        self.team2Catches = []
        self.team1Points = 0
        self.team2Points = 0
        self.trumpReveal = False
        
        self.currentCatch = []
        self.currentSuit = ''
        self.trumpIndice = [0,0,0,0]
        
        self.trumpPlayed = False
        self.trumpSuit = self.playerTrump.suit
        print(f"Trump Suit: {self.trumpSuit}")

        for h in range(8):
            print(f"Catch {h+1} starts now\n")
            if h==7 and self.playerTrump != None:
                 self.players[self.finalBid-1]['cards'].append(self.playerTrump)
                 self.playerTrump = None
            for i in range(4):
                
                print("The cards already played are:")
                self.printCards(self.currentCatch)
                print(f"Player {self.playerChance+1}'s chance to play")
                self.playerChance = self.playerChance%4

                if i==0:

                    if self.players[self.playerChance]['isTrump']:

                        if self.trumpReveal or self.allTrump(self.players[self.playerChance]['cards'],self.trumpSuit):
                            self.selectValidCard(self.players[self.playerChance]['cards'],"00")
                        else:
                            validCards = []
                            for j in range(len(self.players[self.playerChance]['cards'])):
                                if not self.players[self.playerChance]['cards'][j].suit == self.trumpSuit:
                                    validCards.append(self.players[self.playerChance]['cards'][j])
                            
                            self.selectValidCard(validCards,"01")
                    else:
                            
                            self.selectValidCard(self.players[self.playerChance]['cards'],"10")
                else:
                    
                    
                    curSuitInd,trumpSuitInd = self.validCards(self.players[self.playerChance]['cards'],self.currentSuit,self.trumpSuit)
                    if len(curSuitInd)>0:
                            
                            self.selectValidCard(self.players[self.playerChance]['cards'],id="11",init="1",ind=curSuitInd)
                            
                            # print("11Your valid card options are given below, enter the number to choose which card to play:")
                            # cardNum = self.selectCard(self.players[self.playerChance]['cards'],1,curSuitInd)

                            # self.currentCatch.append(self.players[self.playerChance]['cards'][cardNum])
                            # self.players[self.playerChance]['cards'].pop(cardNum)

                            # for j in self.players[self.playerChance]['cards']:
                            #     print(j.identity())
                            # print("\n\n")
                            # self.printCards(self.currentCatch)
                            # print(f"{self.currentSuit}, {self.playerChance}")
                            
                            # self.playerChance+=1
                    else:
                        if not self.trumpReveal:
                            
                            
                            print("Enter 1 to reveal trump or 0 to continue\n")
                            reveal = int(input())

                            if reveal == 1:
                                    
                                    
                                    print("The trump is ",self.playerTrump.identity())
                                    self.trumpReveal = True

                                    if self.playerChance == (self.finalBid-1):
                                         
                                         self.currentCatch.append(self.playerTrump)
                                         self.playerTrump = None
                                         self.trumpPlayed = True

                                         self.trumpIndice[i] = 1
                                         for j in self.players[self.playerChance]['cards']:
                                            print(j.identity())
                                            print("\n\n")
                                            self.printCards(self.currentCatch)
                                            print(f"{self.currentSuit}, {self.playerChance}")
                                    

                                    elif len(trumpSuitInd)>0:            
                                        
                                        self.players[self.finalBid-1]['cards'].append(self.playerTrump)
                                        self.playerTrump = None

                                        self.selectValidCard(self.players[self.playerChance]['cards'],id="12",init="1",ind=trumpSuitInd)
                                        print("12Your valid card options are given below, enter the number to choose which card to play:")
                                        
                                        # cardNum = self.selectCard(self.players[self.playerChance]['cards'],1,trumpSuitInd)
                                        # self.currentCatch.append(self.players[self.playerChance]['cards'][cardNum])
                                        # self.players[self.playerChance]['cards'].pop(cardNum)

                                        # for j in self.players[self.playerChance]['cards']:
                                        #     print(j.identity())
                                        # print("\n\n")
                                        # self.printCards(self.currentCatch)
                                        # print(f"{self.currentSuit}, {self.playerChance}")
                                        
                                        if self.currentSuit != self.trumpSuit:
                                            self.trumpPlayed = True
                                            self.trumpIndice[i] = 1

                                        # self.playerChance+=1
                                    else:
                                        
                                        self.players[self.finalBid-1]['cards'].append(self.playerTrump)
                                        self.playerTrump = None
                                        self.selectValidCard(self.players[self.playerChance]['cards'],id="13",init="1")
                                        # print("13Your valid card options are given below, enter the number to choose which card to play:")
                                        
                                        # cardNum = self.selectCard(self.players[self.playerChance]['cards'])
                                        # self.currentCatch.append(self.players[self.playerChance]['cards'][cardNum])
                                        # self.players[self.playerChance]['cards'].pop(cardNum)

                                        # for j in self.players[self.playerChance]['cards']:
                                        #     print(j.identity())
                                        # print("\n\n")
                                        # self.printCards(self.currentCatch)
                                        # print(f"{self.currentSuit}, {self.playerChance}")

                                        # self.playerChance+=1
                            else:
                                        
                                        self.selectValidCard(self.players[self.playerChance]['cards'],id="14",init="1")
                                        # print("14Your valid card options are given below, enter the number to choose which card to play:")
                                        # cardNum = self.selectCard(self.players[self.playerChance]['cards'])

                                        
                                        # self.currentCatch.append(self.players[self.playerChance]['cards'][cardNum])
                                        # self.players[self.playerChance]['cards'].pop(cardNum)


                                        # for j in self.players[self.playerChance]['cards']:
                                        #     print(j.identity())
                                        # print("\n\n")
                                        # self.printCards(self.currentCatch)
                                        # print(f"{self.currentSuit}, {self.playerChance}")

                                        # self.playerChance+=1
                        else:
                                
                                self.selectValidCard(self.players[self.playerChance]['cards'],id="15",init="2",ind=[i])
                                
                                # print("15Your valid card options are given below, enter the number to choose which card to play:")
                                # cardNum = self.selectCard(self.players[self.playerChance]['cards'])

                                # if(self.players[self.playerChance]['cards'][cardNum].suit == self.trumpSuit) and self.currentSuit != self.trumpSuit:
                                #             self.trumpPlayed = True
                                #             self.trumpIndice[i] = 1

                                # self.currentCatch.append(self.players[self.playerChance]['cards'][cardNum])
                                # self.players[self.playerChance]['cards'].pop(cardNum)

                                # for j in self.players[self.playerChance]['cards']:
                                #         print(j.identity())
                                # print("\n\n")
                                # self.printCards(self.currentCatch)
                                # print(f"{self.currentSuit}, {self.playerChance}")

                                # self.playerChance+=1
            print(len(self.currentCatch))
            maxIndex = 0
            if self.trumpPlayed:
                maxOrder = -1
                count = 0
                points = 0

                for card in self.currentCatch:
                    
                    points += card.points
                    if self.trumpIndice[count] == 1:
                        if card.order > maxOrder:
                            maxOrder = card.order
                            maxIndex = count
                    count+=1

                maxIndex = (self.playerChance-4+maxIndex)%4
                print(f"Player {maxIndex+1} played the highest card, the catch goes to team {self.players[maxIndex]['team']} getting {points} points")
                if self.players[maxIndex]['team'] == 1:
                    self.team1Points += points
                    self.team1Catches.append(self.currentCatch)
                    print(self.team1Points)
                else:
                    self.team2Points += points
                    self.team2Catches.append(self.currentCatch)
                    print(self.team2Points)
            else:
                
                maxOrder = -1
                count = 0
                points = 0

                for card in self.currentCatch:
                    
                    points += card.points
                    if card.suit == self.currentSuit:
                        if card.order > maxOrder:
                            maxOrder = card.order
                            maxIndex = count
                    count+=1
                
                maxIndex = (self.playerChance-4+maxIndex)%4
                print(f"Player {maxIndex+1} played the highest card, the catch goes to team {self.players[maxIndex]['team']} getting {points} points")
                if self.players[maxIndex]['team'] == 1:
                    self.team1Points += points
                    self.team1Catches.append(self.currentCatch)
                    print(self.team1Points)
                else:
                    self.team2Points += points
                    self.team2Catches.append(self.currentCatch)
                    print(self.team2Points)


            self.catches.append(self.currentCatch)
            self.trumpIndice = [0,0,0,0]
            self.trumpPlayed = False
            self.currentCatch = []
            self.playerChance = maxIndex

            print(f"Catch {h+1} is over")
        
        if self.players[self.finalBid-1]['team'] == 1:
             
             if self.team1Points >= self.finalBidValue:
                  print(f"Team 1 has won with a total of {self.team1Points} points")
             else:
                  print(f"Team 2 has beat team 1 with a total of {self.team2Points} points")
        else:
             
             if self.team2Points >= self.finalBidValue:
                  print(f"Team 2 has won with a total of {self.team2Points} points")
             else:
                  print(f"Team 1 has beat team 2 with a total of {self.team1Points} points")

        


env = GameEnv()
env.step(action=0)