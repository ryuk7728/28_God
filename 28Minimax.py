import copy
from cards import Cards
import random
import numpy as np
import pickle

def allTrump(cards,suit):

        for card in cards:
            if card.suit != suit:
                 break
        else:
             return True
        return False

def save_player_cards(filename, p1, p2, p3, p4):
    """
    Saves the four player card arrays to a file.
    """
    players = {
        "player1Cards": p1,
        "player2Cards": p2,
        "player3Cards": p3,
        "player4Cards": p4
    }
    with open(filename, "wb") as f:
        pickle.dump(players, f)
    print(f"Player cards saved to {filename}.")

def load_player_cards(filename):
    """
    Loads the four player card arrays from a file and returns them.
    """
    with open(filename, "rb") as f:
        players = pickle.load(f)
    print(f"Player cards loaded from {filename}.")
    return players["player1Cards"], players["player2Cards"], players["player3Cards"], players["player4Cards"]

def validCard(cards,currentSuit,trumpSuit):
         
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

def printCards(cards):
        for card in cards:
                print(card.identity())

def chance(s):
    return (len(s)+1)

def checkwin(s,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit):
    currentCatch = s
    if len(s)==4:
            maxIndex = 0 # Used to determine which players chance is next
            if trumpPlayed: #If the trump card is played somewhere in the catch
                maxOrder = -1 # Finds which trump is the highest 
                count = 0 # count variable which accounts for index
                points = 0 #Accumulates points

                for card in currentCatch:
                    
                    points += card.points
                    if trumpIndice[count] == 1: # trumpIndice has the indices at which trump was played Eg. [0,1,0,0]
                        if card.order > maxOrder:
                            maxOrder = card.order 
                            maxIndex = count
                    count+=1

                # maxIndex = (playerChance-4+maxIndex)%4 # Does initial player + maxIndex mod 4 to get the highest player
                # print(f"Player {maxIndex+1} played the highest card, the catch goes to team {players[maxIndex]['team']} getting {points} points")
                if players[maxIndex]['team'] == 1:
                    return points
                else:
                    return -1*points
            else:
                # This part of the code explores the case where trump wasnt played
                maxOrder = -1 # Same as earlier
                count = 0
                points = 0

                #Easily understandable- it iterates through all cards to find highest card of the starting suit
                for card in currentCatch:
                    
                    points += card.points
                    if card.suit == currentSuit:
                        if card.order > maxOrder:
                            maxOrder = card.order
                            maxIndex = count
                    count+=1
                

                # maxIndex = (playerChance-4+maxIndex)%4
                # print(f"Player {maxIndex+1} played the highest card, the catch goes to team {players[maxIndex]['team']} getting {points} points")
                if players[maxIndex]['team'] == 1:
                    return points
                else:
                    return -1*points
    else:
        return -100
    
# Verify with rules and add the condition that when its the last trick, and the trump player hasnt revealed his trump then the when its played it behaves like an active trump
def actions(s,players,trumpReveal,trumpSuit,currentSuit,chose,finalBid,playerTrump,trumpPlayed,trumpIndice,reveal=-1):
    playerChance = chance(s)-1
    if  playerChance==0:

        if players[playerChance]['isTrump']:

                        if trumpReveal or allTrump(players[playerChance]['cards'],trumpSuit):
                            return (players[playerChance]['cards'])
                        else:
                            validCards = []
                            for j in range(len(players[playerChance]['cards'])):
                                if not players[playerChance]['cards'][j].suit == trumpSuit:
                                    validCards.append(players[playerChance]['cards'][j])
                            
                            return validCards
        else:
                            
                             return (players[playerChance]['cards'])
    
    else:
                        
                    curSuitInd,trumpSuitInd = validCard(players[playerChance]['cards'],currentSuit,trumpSuit)
                    if len(curSuitInd)>0: #If the player has cards of the current suit, he should play among them
                            
                            validCards = [players[playerChance]['cards'][i] for i in curSuitInd] # Returning the currentsuit cards back in a list
                            return validCards
                            
                            # selectValidCard(players[playerChance]['cards'],init="1",ind=curSuitInd) 
                            
                    else:
                        if not trumpReveal and not chose: # If the player has the option to reveal trump or not and he hasnt chosen then the 2 options is provided as actions
                            return [False,True]
                        
                        elif chose: # In this case the player chose one of the options and its stored in reveal
                            

                            if trumpReveal:
                                    
                                    
                                    # print("The trump is ",self.playerTrump.identity())
                                    # trumpReveal = True

                                    if playerChance == (finalBid-1): #If the current player is the player who put the trump down
                                         
                                        #  print("You have played your trump")
                                        # playerTrump = None
                                        # trumpPlayed = True
                                        # trumpIndice[len(s)] = 1
                                        return [playerTrump]
                                        #  self.currentCatch.append(self.playerTrump)


                                        #  self.trumpIndice[i] = 1
                                        #  for j in self.players[self.playerChance]['cards']:
                                        #     print(j.identity())
                                        #     print("\n\n")
                                        #     self.printCards(self.currentCatch)
                                        #     print(f"{self.currentSuit}, {self.playerChance}")
                                    

                                    elif len(trumpSuitInd)>0:            
                                        
                                        # players[finalBid-1]['cards'].append(playerTrump)
                                        # playerTrump = None
                                        # trumpPlayed = True
                                        # trumpIndice[len(s)] = 1
                                        validCards = [players[playerChance]['cards'][i] for i in trumpSuitInd] # Returning the currentsuit cards back in a list
                                        return validCards                                        


                                    else:
                                        
                                        # players[finalBid-1]['cards'].append(playerTrump)
                                        # playerTrump = None
                                        return players[playerChance]['cards']
                            else:
                                        
                                        return players[playerChance]['cards']

                        else:
                                
                                #Last Case: The card played by minimax should affect the variables related to trumpPlayed and trumpIndice depending on whether the player played a trump card or not
                                return players[playerChance]['cards']
                        

def removeCard(cards,card):
      for k in cards:
            if k.identity() == card.identity():
                cards.remove(k)
                break

def result(s,a,currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid):
    if not (a == True or a == False): # If action taken is card played
        s.append(a)
        # print("The card played is ",a.identity())
        # for s2 in players[len(s)-1]['cards']:
        #     print(s2.identity())
        # print("\n\n")
        # for s1 in s:
        #     print(s1.identity())
        # print("\n\n")
        removeCard(players[len(s)-1]['cards'],a)
        # players[len(s)-1]['cards'].remove(a) #Only applicable in first trick, need to modify for second trick onwards to track whos chance it is
        if len(s)==1: # If its the first card played
            currentSuit = a.suit
            return currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid
        else: #If its 2nd onward card played
            if trumpReveal and a.suit==trumpSuit:
                trumpPlayed = True
                trumpIndice[len(s)-1] = 1

            if a==playerTrump:
                playerTrump = None

            return currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid
    else: # If action taken is choosing or not choosing to reveal trump
        if a and (len(s)+1)!=finalBid: #If player chose to reveal trump and he isnt the trump player then the trump player adds the hidden trump to his cards
            players[finalBid-1]['cards'].append(playerTrump)
            playerTrump = None
        chose = True
        trumpReveal = a
        return currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid

                        

reward_distribution = []
def minimax(s,first,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal):
      
      if checkwin(s,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit)!=-100:
            return checkwin(s,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit)
      
      if chance(s)%2!=0:
          value = -1000
          act = copy.deepcopy(actions(s,players,trumpReveal,trumpSuit,currentSuit,chose,finalBid,playerTrump,trumpPlayed,trumpIndice,reveal))
          chose = False
          for a in act:
                s_copy = copy.deepcopy(s)
                currentSuit_copy = copy.deepcopy(currentSuit)
                trumpReveal_copy = copy.deepcopy(trumpReveal)
                chose_copy = copy.deepcopy(chose) 
                playerTrump_copy = copy.deepcopy(playerTrump)
                trumpPlayed_copy = copy.deepcopy(trumpPlayed)
                trumpIndice_copy = copy.deepcopy(trumpIndice)
                players_copy = copy.deepcopy(players)
               
                currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,a,currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid)
                newtake = minimax(s,False,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal)
                value = max(value,newtake)
                
                s = s_copy
                currentSuit = currentSuit_copy
                trumpReveal = trumpReveal_copy
                chose = chose_copy
                playerTrump = playerTrump_copy
                trumpPlayed = trumpPlayed_copy
                trumpIndice = trumpIndice_copy
                players = players_copy
                
                if first:
                    reward_distribution.append(newtake)
      else:
          value = 1000
          act1 =  copy.deepcopy(actions(s,players,trumpReveal,trumpSuit,currentSuit,chose,finalBid,playerTrump,trumpPlayed,trumpIndice,reveal)) 
          chose = False
          for a in act1:
                s_copy1 = copy.deepcopy(s)
                currentSuit_copy1 = copy.deepcopy(currentSuit)
                trumpReveal_copy1 = copy.deepcopy(trumpReveal)
                chose_copy1 = copy.deepcopy(chose)
                playerTrump_copy1 = copy.deepcopy(playerTrump)
                trumpPlayed_copy1 = copy.deepcopy(trumpPlayed)
                trumpIndice_copy1 = copy.deepcopy(trumpIndice)
                players_copy1 = copy.deepcopy(players)
                
                currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,a,currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid)
                value = min(value,minimax(s,False,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal))
                
                s = s_copy1
                currentSuit = currentSuit_copy1
                trumpReveal = trumpReveal_copy1
                chose = chose_copy1
                playerTrump = playerTrump_copy1
                trumpPlayed = trumpPlayed_copy1
                trumpIndice = trumpIndice_copy1
                players = players_copy1
                
                if first:
                    reward_distribution.append(value)
                
      
      return value
            




# cards = Cards.packOf28()    
# random.shuffle(cards)

# player1Cards = cards[0:8]
# player2Cards = cards[8:16]
# player3Cards = cards[16:24]
# player4Cards = cards[24:32]

# print("Player 1:")
# printCards(player1Cards)
# print("\n")
# printCards(player2Cards)
# print("\n")
# printCards(player3Cards)
# print("\n")
# printCards(player4Cards)

# # Save the player card arrays to a file
# save_player_cards(save_filename, player1Cards, player2Cards, player3Cards, player4Cards)

# Later on (or in another program run) you can load the player card arrays back:
save_filename = "player_cards.pkl"
loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards = load_player_cards(save_filename)

x = copy.deepcopy(loaded_player1Cards)

x1 = copy.deepcopy(loaded_player2Cards)
# x2 = copy.deepcopy(loaded_player3Cards)
# x3 = copy.deepcopy(loaded_player4Cards)

# avg_rewards = np.array([0,0,0,0,0,0,0,0])
remainingCards = loaded_player2Cards+loaded_player3Cards+loaded_player4Cards
# remainingCards = loaded_player3Cards+loaded_player4Cards
sample_size = 300
for j in range(sample_size):
    
    random.shuffle(remainingCards)
    # print(len(remainingCards))

    loaded_player1Cards = copy.deepcopy(x)
    # loaded_player2Cards = copy.deepcopy(x1)
    loaded_player2Cards = copy.deepcopy(remainingCards[0:8])
    loaded_player3Cards = copy.deepcopy(remainingCards[8:16])
    loaded_player4Cards = copy.deepcopy(remainingCards[16:24])

    # print("\nLoaded Player 1 Cards:")
    # printCards(loaded_player1Cards)
    # print("\nLoaded Player 2 Cards:")
    # printCards(loaded_player2Cards)
    # print("\nLoaded Player 3 Cards:")
    # printCards(loaded_player3Cards)
    # print("\nLoaded Player 4 Cards:")
    # printCards(loaded_player4Cards)

    s = []
    # s = [copy.deepcopy(x[1])]
    finalBid = 3
    rand_int = random.randint(0,7)
    playerTrump = loaded_player3Cards[rand_int]
    loaded_player3Cards.remove(playerTrump)
    playerCards = [loaded_player1Cards,loaded_player2Cards,loaded_player3Cards,loaded_player4Cards]
    players = []



    for i in range(4):
                    player = {'cards':playerCards[i],'isTrump':i==(finalBid-1),'team':1 if i % 2 == 0 else 2, 'trump':playerTrump if i==(finalBid-1) else None}
                    players.append(player)

    trumpReveal = False
    trumpSuit = playerTrump.suit
    # currentSuit = "Hearts"
    currentSuit = ""
    chose = False
    trumpPlayed = False
    trumpIndice = [0,0,0,0]
    reveal = -1
    currentCatch = []
    playerChance = 0


    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal)
    # print(reward_distribution)
    if j==0:
        avg_rewards = np.array(reward_distribution)
    else:
        avg_rewards = np.array(reward_distribution)+avg_rewards



# print("Loaded Player 1 Cards:")
# printCards(x)
# print("\n\n")
# print("Loaded Player 2 Cards:")
# printCards(x1)
# print("\n\n")
# print("Loaded Player 3 Cards:")
# printCards(x2)
# print("\n\n")
# print("Loaded Player 4 Cards:")
# printCards(x3)
# print("\n\n")
# print("Reward Distribution: Values")

printCards(x)
print(avg_rewards/sample_size)


    