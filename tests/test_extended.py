from src.ai.minimax import minimax_extended
from src.ai.minimax import result
from src.cards import Cards
import copy
from tests.sample_hands.example_hands import get_game3
import math
import random
from collections import defaultdict
import time

def reset(currentSuit,s,trumpPlayed,trumpIndice,chose):
       currentSuit = ""
       s = []
       trumpPlayed = False
       trumpIndice = [0,0,0,0]
       chose = False

       return currentSuit,s,trumpPlayed,trumpIndice,chose


def create_dictionary(p1,p2,p3,p4,finalBid,playerTrump):
        playerCards = [p1,p2,p3,p4]
        players = []
        for i in range(4):
                player = {'cards':copy.deepcopy(playerCards[i]),'isTrump':i==(finalBid-1),'team':1 if i % 2 == 0 else 2, 'trump':playerTrump if i==(finalBid-1) else None}
                players.append(player)
        return players
        

def printCards(cards):
        for card in cards:
                print(card.identity())

def returnTrump(known,players,finalBid,trumpSuit):
      if not known:
            card = players[finalBid]['cards'].pop(0)
            return card,card.suit
      else:
            return None,trumpSuit

def P1(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,total=0,num=0):
    cards = defaultdict(int)
    if finalBid == 1 or playerTrump is None:
        full_cards = loaded_player2Cards+loaded_player3Cards+loaded_player4Cards
    else:
          full_cards = loaded_player2Cards+loaded_player3Cards+loaded_player4Cards+[playerTrump]
    l2 = len(loaded_player2Cards)
    l3 = len(loaded_player3Cards)+l2
    l4 = len(loaded_player4Cards)+l3
    for i in range(500):
        random.shuffle(full_cards)
        loaded_player2Cards = full_cards[0:l2]
        loaded_player3Cards = full_cards[l2:l3]
        loaded_player4Cards = full_cards[l3:l4]
        players = create_dictionary(loaded_player1Cards,loaded_player2Cards,loaded_player3Cards,loaded_player4Cards,finalBid,playerTrump)
        trumpSuit = "Clubs"
        reward_distribution = []
        minimax_extended(s,True,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution,total,num,k,-math.inf,math.inf)
        for x in reward_distribution:
              cards[x[0]]+=1/len(reward_distribution)
        # cards[reward_distribution[0][0]]+=1
    best = ""
    freq = -1
    for k1,v in cards.items():
        if v>freq:
                freq = v
                best = k1
    print(best,freq/500)

def P3(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0):
    cards = defaultdict(int)
    if finalBid == 3 or playerTrump is None:
        full_cards = loaded_player1Cards+loaded_player2Cards+loaded_player4Cards
    else:
          full_cards = loaded_player1Cards+loaded_player2Cards+loaded_player4Cards+[playerTrump]
    l1 = len(loaded_player1Cards)
    l2 = len(loaded_player2Cards)+l1
    l4 = len(loaded_player4Cards)+l2
    for i in range(500):
        random.shuffle(full_cards)
        loaded_player1Cards = full_cards[0:l1]
        loaded_player2Cards = full_cards[l1:l2]
        loaded_player4Cards = full_cards[l2:l4]
        players = create_dictionary(loaded_player1Cards,loaded_player2Cards,loaded_player3Cards,loaded_player4Cards,finalBid,playerTrump)
        playerTrump,trumpSuit = returnTrump(known,players,finalBid,trumpSuit)
        reward_distribution = []
        minimax_extended(s,True,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution,total,num,k,-math.inf,math.inf)
        for x in reward_distribution:
              cards[x[0]]+=1/len(reward_distribution)
    best = ""
    freq = -1
    for k1,v in cards.items():
        if v>freq:
                freq = v
                best = k1
    print(best,freq/500)
        
def test_minimax_game1(cards):
    loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards = get_game3()
    full_cards = loaded_player2Cards+loaded_player3Cards+loaded_player4Cards
    random.shuffle(full_cards)
    loaded_player2Cards = full_cards[0:8]
    loaded_player3Cards = full_cards[8:16]
    loaded_player4Cards = full_cards[16:24]
    finalBid = 1
    playerTrump = loaded_player1Cards.pop(2)
    players = create_dictionary(loaded_player1Cards,loaded_player2Cards,loaded_player3Cards,loaded_player4Cards,finalBid,playerTrump)
    trumpReveal = False
    trumpSuit = playerTrump.suit
    currentSuit = ""
    chose = False
    trumpPlayed = False
    trumpIndice = [0,0,0,0]
    reveal = -1
    currentCatch = []
    playerChance = 0
    reward_distribution = []
    s = []
    total = 0
    num = 0
    k = 2

    minimax_extended(s,True,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution,total,num,k,-math.inf,math.inf)
    cards[reward_distribution[0][0]]+=1

loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards = get_game3()
finalBid = 1
playerTrump = loaded_player1Cards.pop(2)
trumpReveal = False
trumpSuit = playerTrump.suit
currentSuit = ""
chose = False
trumpPlayed = False
trumpIndice = [0,0,0,0]
reveal = -1
currentCatch = []
playerChance = 0
k = 2
s=[]
known = False
cards = defaultdict(int)
players = create_dictionary(loaded_player1Cards,loaded_player2Cards,loaded_player3Cards,loaded_player4Cards,finalBid,playerTrump)
# P1(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k)

currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player1Cards.pop(6),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player2Cards.pop(5),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
P3(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player3Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player4Cards.pop(7),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
# playerChance = 2

# # P3(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player3Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# known = True
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,True,currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# loaded_player1Cards =  players[0]['cards']
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player4Cards.pop(4),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# # P1(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k)
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player1Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player2Cards.pop(5),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
# playerChance = 0

# # P1(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k)
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player1Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player2Cards.pop(4),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# # P3(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player3Cards.pop(5),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player4Cards.pop(3),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
# playerChance = 0

# k=2
# # P1(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k)
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player1Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player2Cards.pop(3),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# # P3(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player3Cards.pop(1),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player4Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
# playerChance = 1

# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player2Cards.pop(3),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# k=3
# # P3(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player3Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player4Cards.pop(1),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# # P1(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k)
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player1Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
# playerChance = 0

# # P1(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k)
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player1Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player2Cards.pop(1),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# P3(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player3Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player4Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
# playerChance = 3
# k=2
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player4Cards.pop(1),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# P1(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k)
# #WHYYYYYYY ABOVE IT DIDNT PLAY ACE OF CLUBS CHECKKKKKKK
# # currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player1Cards.pop(1),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# # currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player2Cards.pop(1),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# # # P3(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
# # currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player3Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# # currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
# # playerChance = 0

# # P1(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k)
# # currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player1Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# # currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player2Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# # P3(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
# # currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player3Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# # currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player4Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# # print()


# # known = True #Trump was revealed now
# # currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,True,currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# # loaded_player1Cards =  players[0]['cards']
# # P3(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)

# # currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player3Cards.pop(7),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# # currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player4Cards.pop(2),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# # currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
# # playerChance = 2

# # P3(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
# # currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player3Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# # currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player4Cards.pop(6),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# # P1(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k)
# # currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player1Cards.pop(5),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# # currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player2Cards.pop(5),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# # currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
# # playerChance = 2

# # P3(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
# # currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player3Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# # currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player4Cards.pop(5),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# # k=3
# # P1(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k)


# # # print(time.time())
# # # cards = defaultdict(int)

# # # for i in range(500):
# # #         test_minimax_game1(cards)

# # # print(time.time())

# # # best = ""
# # # freq = -1
# # # for k,v in cards.items():
# # #        if v>freq:
# # #               freq = v
# # #               best = k
# # # print(best,freq/500)
       
