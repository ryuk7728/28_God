from src.ai.minimax import minimax,minimax_alpha
from src.ai.minimax import result
import copy
from tests.sample_hands.example_hands import get_game1,get_game2
from tests.sample_hands.special_cases import get_special_case1,get_special_case2,get_special_case3

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
    reward_alpha = []
    s = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player1Cards.pop(5),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]
    
    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player2Cards.pop(7),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,False,currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player3Cards.pop(4),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player4Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player1Cards.pop(2),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,True,currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player2Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player3Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player4Cards.pop(3),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
    reward_distribution = []
    playerChance = 1
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player2Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player3Cards.pop(5),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player4Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player1Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
    playerChance = 0
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player1Cards.pop(1),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player2Cards.pop(3),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player3Cards.pop(4),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player4Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
    playerChance = 0
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    
    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,players[0]['cards'][3],currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,players[1]['cards'][3],currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,players[2]['cards'][3],currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,players[3]['cards'][0],currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
    playerChance = 0
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,players[0]['cards'][2],currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,players[1]['cards'][0],currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,players[2]['cards'][0],currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,players[3]['cards'][0],currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
    playerChance = 0
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,players[0]['cards'][0],currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,players[1]['cards'][0],currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,players[2]['cards'][0],currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,players[3]['cards'][1],currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
    playerChance = 0
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,players[0]['cards'][0],currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,players[1]['cards'][0],currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,players[2]['cards'][0],currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]


def test_minimax_special_case1():
    loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards = get_special_case1()
    finalBid = 1
    playerTrump = loaded_player1Cards.pop(0)
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
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

def test_minimax_special_case2():
    loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards = get_special_case2()
    finalBid = 1
    playerTrump = loaded_player1Cards.pop(0)
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
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

def test_minimax_special_case3():
    loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards = get_special_case3()
    finalBid = 2
    playerTrump = loaded_player2Cards.pop(0)
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
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

def test_minimax_game2():
    loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards = get_game2()
    finalBid = 2
    playerTrump = loaded_player2Cards.pop(3)
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
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player1Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player2Cards.pop(4),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player3Cards.pop(2),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player4Cards.pop(2),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
    playerChance = 0
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player1Cards.pop(2),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player2Cards.pop(5),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player3Cards.pop(5),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player4Cards.pop(5),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
    playerChance = 1
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player2Cards.pop(2),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player3Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player4Cards.pop(2),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player1Cards.pop(1),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
    playerChance = 2
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player3Cards.pop(1),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player4Cards.pop(2),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,True,currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player1Cards.pop(3),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player2Cards.pop(1),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
    playerChance = 1
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]
    
    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player2Cards.pop(2),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player3Cards.pop(1),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player4Cards.pop(2),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player1Cards.pop(1),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
    playerChance = 3
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player4Cards.pop(2),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player1Cards.pop(2),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    loaded_player2Cards = players[1]['cards']

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player2Cards.pop(2),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player3Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
    playerChance = 1
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player2Cards.pop(1),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player3Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player4Cards.pop(1),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player1Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
    playerChance = 2
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player3Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player4Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid = result(s,loaded_player1Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
    reward_distribution = []
    minimax(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution)
    reward_alpha = []
    minimax_alpha(s,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_alpha)
    if (playerChance+len(s))%2==0:
        assert max(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0] 
    else:
        assert min(reward_distribution, key=lambda t: t[1])[0] == reward_alpha[0][0]

    



    
test_minimax_game1()
# test_minimax_game2()

