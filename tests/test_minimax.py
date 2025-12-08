from src.ai.minimax import minimax
from src.ai.minimax import result
import copy
from tests.sample_hands.example_hands import get_game1

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


def test_minimax_game1():
    loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards = get_game1()
    finalBid = 1
    playerTrump = loaded_player1Cards.pop(1)
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
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    assert reward_distribution == [-3,8,-4]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player1Cards.pop(5),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    assert reward_distribution == [8]
    
    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player2Cards.pop(7),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    assert reward_distribution == [8,8]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,False,currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    assert reward_distribution == [5,5,5,5,8,6,7,5]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player3Cards.pop(4),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    assert reward_distribution == [8,8,9,8]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player4Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    assert reward_distribution == [-4,-5]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player1Cards.pop(2),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    assert reward_distribution == [-4,-3]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,True,currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    assert reward_distribution == [-3,-1,-1]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player2Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    assert reward_distribution == [-3,-3,-3,-3,-4,-5,-3]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player3Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    assert reward_distribution == [-2,-3,-2]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player4Cards.pop(3),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
    reward_distribution = []
    playerChance = 1
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    assert reward_distribution == [4,4,6,6,5,5]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player2Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    assert reward_distribution == [4]



test_minimax_game1()

