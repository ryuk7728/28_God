from src.ai.minimax import minimax_extended
from src.ai.minimax import result
import copy
from tests.sample_hands.example_hands import get_game1,get_game2
from tests.sample_hands.special_cases import get_special_case1,get_special_case2,get_special_case3
import math

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


# def test_minimax_game1():
#     loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards = get_game1()
#     finalBid = 1
#     playerTrump = loaded_player1Cards.pop(1)
#     players = create_dictionary(loaded_player1Cards,loaded_player2Cards,loaded_player3Cards,loaded_player4Cards,finalBid,playerTrump)
#     trumpReveal = False
#     trumpSuit = playerTrump.suit
#     currentSuit = ""
#     chose = False
#     trumpPlayed = False
#     trumpIndice = [0,0,0,0]
#     reveal = -1
#     currentCatch = []
#     playerChance = 0
#     reward_distribution = []
#     s = []
#     total = 0
#     num = 0
#     k = 2
#     minimax_extended(s,True,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution,total,num,k,-math.inf,math.inf)
#     print("Done")

# test_minimax_game1()
