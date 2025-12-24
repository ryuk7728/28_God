from src.ai.minimax import minimax_extended
from src.ai.minimax import result
from src.cards import Cards
import copy
from tests.sample_hands.example_hands import get_game4
import math
import random
from collections import defaultdict
import time

random.seed(42)

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
            card = players[finalBid-1]['cards'].pop(0)
            return card,card.suit
      else:
            return None,trumpSuit

def addTrump(crds,finalB,p3):
      if finalB == 4:
            finalB = 2
      else:
            if p3:
                finalB-=1
            else:
                finalB-=2
      for i in range(len(crds)):
            if i>=finalB:
                  crds[i]+=1
      return crds[0],crds[1],crds[2]

# def P1(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,total=0,num=0):
#     cards = defaultdict(int)
#     if finalBid == 1 or playerTrump is None:
#         full_cards = loaded_player2Cards+loaded_player3Cards+loaded_player4Cards
#     else:
#           full_cards = loaded_player2Cards+loaded_player3Cards+loaded_player4Cards+[playerTrump]
#     l2 = len(loaded_player2Cards)
#     l3 = len(loaded_player3Cards)+l2
#     l4 = len(loaded_player4Cards)+l3
#     for i in range(500):
#         random.shuffle(full_cards)
#         loaded_player2Cards = full_cards[0:l2]
#         loaded_player3Cards = full_cards[l2:l3]
#         loaded_player4Cards = full_cards[l3:l4]
#         players = create_dictionary(loaded_player1Cards,loaded_player2Cards,loaded_player3Cards,loaded_player4Cards,finalBid,playerTrump)
#         trumpSuit = "Clubs"
#         reward_distribution = []
#         minimax_extended(s,True,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution,total,num,k,-math.inf,math.inf)
#         for x in reward_distribution:
#               cards[x[0]]+=1/len(reward_distribution)
#         # cards[reward_distribution[0][0]]+=1
#     best = ""
#     freq = -1
#     for k1,v in cards.items():
#         if v>freq:
#                 freq = v
#                 best = k1
#     print(best,freq/500)

def print_sequences(iteration, total_iterations, best_value, sequences):
    """Print all sequences that achieve the best value."""
    print("\n" + "=" * 50)
    print(f"Monte Carlo Iteration {iteration}/{total_iterations}")
    print("=" * 50)
    print(f"Best Total: {best_value:+d}")
    print(f"Found {len(sequences)} sequence(s) achieving best total\n")
    
    for seq_idx, sequence in enumerate(sequences, 1):
        print(f"--- Sequence {seq_idx} of {len(sequences)} achieving best total ---")
        
        for trick in sequence:
            print(f"Trick {trick['trick_num']}:")
            for card_play in trick['cards']:
                print(f"  P{card_play['player']} plays: {card_play['card']}")
            print(f"  → Winner: P{trick['winner']}, Points: {trick['points']:+d}")
            print()
    
    print("=" * 50)


# Modified P1 function
def P1(cards, loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,
       finalBid, trumpSuit, trumpReveal, currentSuit, chose, trumpPlayed, trumpIndice, reveal,
       currentCatch, playerChance, s, playerTrump, k, known, total=0, num=0):
    
    cards = defaultdict(int)
    
    if finalBid == 1 or playerTrump is None:
        full_cards = loaded_player2Cards + loaded_player3Cards + loaded_player4Cards
    else:
        full_cards = loaded_player2Cards + loaded_player3Cards + loaded_player4Cards + [playerTrump]
    
    l2 = len(loaded_player2Cards)
    l3 = len(loaded_player3Cards) + l2
    l4 = len(loaded_player4Cards) + l3
    
    if playerTrump is not None and finalBid != 1:
        l2, l3, l4 = addTrump([l2, l3, l4], finalBid, False)
    
    for i in range(500):
        random.shuffle(full_cards)
        sim_player2Cards = full_cards[0:l2]
        sim_player3Cards = full_cards[l2:l3]
        sim_player4Cards = full_cards[l3:l4]
        
        players = create_dictionary(loaded_player1Cards, sim_player2Cards, sim_player3Cards, 
                                    sim_player4Cards, finalBid, playerTrump)
        sim_playerTrump, sim_trumpSuit = returnTrump(known, players, finalBid, trumpSuit)
        
        reward_distribution = []
        
        # Call modified minimax
        best_value, sequences = minimax_extended(
            s, True, True, trumpPlayed, currentCatch, trumpIndice, playerChance, players,
            currentSuit, trumpReveal, sim_trumpSuit, chose, finalBid, sim_playerTrump,
            reveal, reward_distribution, total, num, k, -math.inf, math.inf
        )
        
        # Print sequences for this rollout
        print_sequences(i + 1, 500, best_value, sequences)
        
        # Still collect vote distribution
        if reward_distribution:
            for x in reward_distribution:
                cards[x[0]] += 1.0 / len(reward_distribution)
    
    # Find and return best card
    best = ""
    freq = -1
    for card_id, vote_count in cards.items():
        if vote_count > freq:
            freq = vote_count
            best = card_id
    
    print(f"\nFinal Recommendation: {best} (confidence: {freq/500:.1%})")
    return best


# Modified P3 function (similar structure)
def P3(cards, loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,
       finalBid, trumpSuit, trumpReveal, currentSuit, chose, trumpPlayed, trumpIndice, reveal,
       currentCatch, playerChance, s, playerTrump, k, known, total=0, num=0):
    
    cards = defaultdict(int)
    
    if finalBid == 3 or playerTrump is None:
        full_cards = loaded_player1Cards + loaded_player2Cards + loaded_player4Cards
    else:
        full_cards = loaded_player1Cards + loaded_player2Cards + loaded_player4Cards + [playerTrump]
    
    l1 = len(loaded_player1Cards)
    l2 = len(loaded_player2Cards) + l1
    l4 = len(loaded_player4Cards) + l2
    
    if playerTrump is not None and finalBid != 3:
        l1, l2, l4 = addTrump([l1, l2, l4], finalBid, True)
    
    for i in range(500):
        random.shuffle(full_cards)
        sim_player1Cards = full_cards[0:l1]
        sim_player2Cards = full_cards[l1:l2]
        sim_player4Cards = full_cards[l2:l4]
        
        players = create_dictionary(sim_player1Cards, sim_player2Cards, loaded_player3Cards,
                                    sim_player4Cards, finalBid, playerTrump)
        sim_playerTrump, sim_trumpSuit = returnTrump(known, players, finalBid, trumpSuit)
        
        reward_distribution = []
        
        # Call modified minimax
        best_value, sequences = minimax_extended(
            s, True, True, trumpPlayed, currentCatch, trumpIndice, playerChance, players,
            currentSuit, trumpReveal, sim_trumpSuit, chose, finalBid, sim_playerTrump,
            reveal, reward_distribution, total, num, k, -math.inf, math.inf
        )
        
        # Print sequences for this rollout
        print_sequences(i + 1, 500, best_value, sequences)
        
        # Still collect vote distribution
        if reward_distribution:
            for x in reward_distribution:
                cards[x[0]] += 1.0 / len(reward_distribution)
    
    # Find and return best card
    best = ""
    freq = -1
    for card_id, vote_count in cards.items():
        if vote_count > freq:
            freq = vote_count
            best = card_id
    
    print(f"\nFinal Recommendation: {best} (confidence: {freq/500:.1%})")
    return best

# def P3(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0):
#     cards = defaultdict(int)
#     if finalBid == 3 or playerTrump is None:
#         full_cards = loaded_player1Cards+loaded_player2Cards+loaded_player4Cards
#     else:
#           full_cards = loaded_player1Cards+loaded_player2Cards+loaded_player4Cards+[playerTrump]
    
#     l1 = len(loaded_player1Cards)
#     l2 = len(loaded_player2Cards)+l1
#     l4 = len(loaded_player4Cards)+l2
#     if playerTrump is not None and finalBid!=3:
#           l1,l2,l4 = addTrump([l1,l2,l4],finalBid,True)
#     for i in range(500):
#         print("NEWWWWWWWWWW!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#         random.shuffle(full_cards)
#         loaded_player1Cards = full_cards[0:l1]
#         loaded_player2Cards = full_cards[l1:l2]
#         loaded_player4Cards = full_cards[l2:l4]
#         players = create_dictionary(loaded_player1Cards,loaded_player2Cards,loaded_player3Cards,loaded_player4Cards,finalBid,playerTrump)
#         playerTrump,trumpSuit = returnTrump(known,players,finalBid,trumpSuit)
#         reward_distribution = []
#         minimax_extended(s,True,True,trumpPlayed,currentCatch,trumpIndice,playerChance,players,currentSuit,trumpReveal,trumpSuit,chose,finalBid,playerTrump,reveal,reward_distribution,total,num,k,-math.inf,math.inf)
#         for x in reward_distribution:
#               cards[x[0]]+=1/len(reward_distribution)
#     best = ""
#     freq = -1
#     for k1,v in cards.items():
#         if v>freq:
#                 freq = v
#                 best = k1
#     print(cards)
#     print(best,freq/500)

loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards = get_game4()
finalBid = 2
playerTrump = loaded_player2Cards.pop(7)
trumpReveal = False
trumpSuit = playerTrump.suit
currentSuit = ""
chose = False
trumpPlayed = False
trumpIndice = [0,0,0,0]
reveal = -1
currentCatch = []
playerChance = 1
k = 2
s=[]
known = False
cards = defaultdict(int)
players = create_dictionary(loaded_player1Cards,loaded_player2Cards,loaded_player3Cards,loaded_player4Cards,finalBid,playerTrump)

currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player2Cards.pop(6),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# P3(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player3Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player4Cards.pop(5),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# P1(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player1Cards.pop(6),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
playerChance = 2

P3(cards, loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,
       finalBid, trumpSuit, trumpReveal, currentSuit, chose, trumpPlayed, trumpIndice, reveal,
       currentCatch, playerChance, s, playerTrump, k, known, 0, 0)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player3Cards.pop(4),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player4Cards.pop(3),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# P1(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player1Cards.pop(1),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,True,currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# loaded_player2Cards =  players[1]['cards']
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,playerTrump,currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
known = True
currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
playerChance = 1

currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player2Cards.pop(4),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# P3(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player3Cards.pop(2),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player4Cards.pop(2),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# P1(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player1Cards.pop(2),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
playerChance = 2

# P3(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player3Cards.pop(3),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player4Cards.pop(2),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# P1(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player1Cards.pop(1),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player2Cards.pop(2),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
playerChance = 1


currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player2Cards.pop(3),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
k=4
# P3(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player3Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player4Cards.pop(3),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# P1(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player1Cards.pop(3),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
playerChance = 3

k=3
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player4Cards.pop(1),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# P1(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player1Cards.pop(1),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player2Cards.pop(2),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# P3(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player3Cards.pop(1),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
playerChance = 2

k=2
# P3(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player3Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player4Cards.pop(1),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# P1(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player1Cards.pop(1),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player2Cards.pop(1),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
currentSuit,s,trumpPlayed,trumpIndice,chose = reset(currentSuit,s,trumpPlayed,trumpIndice,chose)
playerChance = 1

k=1
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player2Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
P3(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player3Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player4Cards.pop(0),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
P1(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)


# k=2



# # P1(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k)

# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player1Cards.pop(6),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# currentSuit,s,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid, _ = result(s,loaded_player2Cards.pop(5),currentSuit,trumpReveal,chose,playerTrump,trumpPlayed,trumpIndice,players,trumpSuit,finalBid,playerChance)
# # P3(cards,loaded_player1Cards, loaded_player2Cards, loaded_player3Cards, loaded_player4Cards,finalBid,trumpSuit,trumpReveal,currentSuit,chose,trumpPlayed,trumpIndice,reveal,currentCatch,playerChance,s,playerTrump,k,known,total=0,num=0)
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

